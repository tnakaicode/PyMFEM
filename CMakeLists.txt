cmake_minimum_required(VERSION 3.0.0)
project(PyMFEM VERSION 0.1.0)

include(CTest)
enable_testing()

set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
include(CPack)

if(NOT DEFINED PYTHONOCC_BUILD_TYPE)
  set(PYTHONOCC_BUILD_TYPE "Release" CACHE STRING "Build type") # By default set release build
endif(NOT DEFINED PYTHONOCC_BUILD_TYPE)
set(CMAKE_BUILD_TYPE ${PYTHONOCC_BUILD_TYPE} CACHE INTERNAL "Build type, immutable" FORCE)

set(BUILD_SHARED_LIBS ON)
include_directories(${CMAKE_CURRENT_SOURCE_DIR})

#############################
# Option_With_Default macro #
#############################
macro(option_with_default OPTION_NAME OPTION_STRING OPTION_DEFAULT)
  option(${OPTION_NAME} ${OPTION_STRING} ${OPTION_DEFAULT})
endmacro(option_with_default OPTION_NAME OPTION_STRING OPTION_DEFAULT)

#################
# Build options #
#################
# include(${CMAKE_CURRENT_SOURCE_DIR}/cmake/OCE_Modules.cmake)
# add an option to choose toolkits to compile
option_with_default(SWIG_HIDE_WARNINGS "Check this option if you want a less verbose swig output." ON)

############
# Python 3 #
############
find_package(Python3 COMPONENTS Interpreter Development NumPy REQUIRED)
include_directories(${Python3_NumPy_INCLUDE_DIRS})
message(STATUS "Numpy include directory: ${Python3_NumPy_INCLUDE_DIRS}")
#set(CMAKE_SWIG_FLAGS ${CMAKE_SWIG_FLAGS} -DBUILD_MESHDS_NUMPY)
message(STATUS "Python3 interpreter:" ${Python3_EXECUTABLE})
message(STATUS "Python include directory: ${Python3_INCLUDE_DIRS}")
message(STATUS "Python library release: ${Python3_LIBRARY_RELEASE}")

########
# SWIG #
########
find_package(SWIG 4.0.2 REQUIRED)
include(${SWIG_USE_FILE})
set(SWIG_FILES_PATH "${mfem/common};${mfem/_ser}")
set(CMAKE_SWIG_FLAGS ${CMAKE_SWIG_FLAGS} -fvirtual -py3)
if(SWIG_HIDE_WARNINGS)
  message(STATUS "Disabled SWIG warnings")
  set(CMAKE_SWIG_FLAGS ${CMAKE_SWIG_FLAGS} -w302,401,402,412,314,509,512,504,325,503,520,350,351,383,389,394,395,404)
endif()

################################
# MFEM include and lib location #
################################
if(MFEM_HIDE_DEPRECATED)
  message(STATUS "Disabled deprecation warnings for MFEM")
  add_definitions(-DOCCT_NO_DEPRECATED)
endif(MFEM_HIDE_DEPRECATED)

if(DEFINED MFEM_INCLUDE_PATH)
  if(NOT DEFINED MFEM_LIB_PATH)
    message(FATAL_ERROR "MFEM_LIB_PATH must be defined")
  endif(NOT DEFINED MFEM_LIB_PATH)
  set(MFEM_INCLUDE_PATH ${MFEM_INCLUDE_PATH} CACHE PATH "MFEM include path")
  set(MFEM_LIB_PATH ${MFEM_LIB_PATH} CACHE PATH "MFEM lib path")
  include_directories(${MFEM_INCLUDE_PATH})
  link_directories(${MFEM_LIB_PATH})
# if MFEM_INCLUDE_PATH is not passed at command line,
# find MFEM automatically
else(MFEM_INCLUDE_PATH)
  find_package(MFEM 4.5.1 REQUIRED)
  if(MFEM_FOUND)
    message(STATUS "MFEM version found: " ${MFEM_MAJOR_VERSION} "." ${MFEM_MINOR_VERSION} "." ${MFEM_MAINTENANCE_VERSION})
    message(STATUS "MFEM include directory: " ${MFEM_INCLUDE_DIR})
    message(STATUS "MFEM library directory: " ${MFEM_LIBRARY_DIR})
    include_directories(${MFEM_INCLUDE_DIR})
  else(MFEM_FOUND)  # set default paths
    set(MFEM_INCLUDE_PATH /usr/local/include/MFEM CACHE PATH "MFEM include path")
    set(MFEM_LIB_PATH /usr/local/lib CACHE PATH "MFEM lib path")
    include_directories(${MFEM_INCLUDE_PATH})
    link_directories(${MFEM_LIB_PATH})
  endif(MFEM_FOUND)
endif(DEFINED MFEM_INCLUDE_PATH)

###############################################
# Installation directory                      #
# by default, installed to site-packages/mfem #
###############################################
if(NOT DEFINED PyMFEM_INSTALL_DIRECTORY)
    if(DEFINED ENV{SP_DIR} AND WIN32)
      # TODO: following hack is azure specific, a recent update in azure
      # prevent cmake to find correct paths of python3 on windows
      # this should be removed as soon as possible
      message(STATUS "conda-build running, using $ENV{SP_DIR} as install dir")
      set(PyMFEM_INSTALL_DIRECTORY $ENV{SP_DIR}/mfem CACHE PATH "PyMFEM install directory")
    else(DEFINED ENV{SP_DIR} AND WIN32)
      execute_process(COMMAND ${Python3_EXECUTABLE} -c "from distutils.sysconfig import get_python_lib; from os.path import relpath; print(relpath(get_python_lib(1,prefix='${CMAKE_INSTALL_PREFIX}'),'${CMAKE_INSTALL_PREFIX}'))" OUTPUT_VARIABLE python_lib OUTPUT_STRIP_TRAILING_WHITESPACE)
      set(PyMFEM_INSTALL_DIRECTORY ${python_lib}/mfem CACHE PATH "PyMFEM install directory")
    endif(DEFINED ENV{SP_DIR} AND WIN32)
endif(NOT DEFINED PyMFEM_INSTALL_DIRECTORY)

message(STATUS "PyMFEM modules will be installed to: ${PyMFEM_INSTALL_DIRECTORY}")

################
# Headers path #
################
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/headers)

################################################
# Define output path for generated libraries:  #
# platform/compiler-build_type-bits            #
# for instance:                                #
#     ./win32/bin/vc7.1-release-64             #
#     ./win32/bin/vc9-debug-32                 #
#     ./Unix/i386-debug-64                     #
################################################
if(WIN32)
  if(MSVC) # The compiler used is MSVC
    message(STATUS "Found MSVC compiler: ${MSVC} ${MSVC_VERSION}")
    set(LIBRARY_OUTPUT_PATH bin/)
    # prevent bigobj fatal error C1148 issue, and remove C4244 verbose warning
    add_definitions("/bigobj /wd4244 /wd4251 /wd4275 /wd4290")
  elseif (BORLAND) # The compiler used is BORLAND
    set(LIBRARY_OUTPUT_PATH win${BIT}/bin/${CMAKE_BUILD_TYPE})
  else()
    set(LIBRARY_OUTPUT_PATH win${BIT}/bin/${CMAKE_BUILD_TYPE})
  endif()
  set(EXECUTABLE_OUTPUT_PATH ${LIBRARY_OUTPUT_PATH})
else(WIN32)
  set(LIBRARY_OUTPUT_PATH ${PLATFORM}/${CMAKE_SYSTEM_PROCESSOR}-${CMAKE_BUILD_TYPE}-${BIT})
endif(WIN32)
set(CMAKE_SWIG_OUTDIR ${LIBRARY_OUTPUT_PATH})

##################
# Common Module  #
##################
file(MAKE_DIRECTORY ${CMAKE_BINARY_DIR}/${mfen/common})
set(FILE ${SWIG_FILES_PATH}/${OCE_MODULE}.i)
set_source_files_properties(${FILE} PROPERTIES CPLUSPLUS ON)
swig_add_library (${OCE_MODULE} LANGUAGE python SOURCES ${FILE} TYPE MODULE)
swig_link_libraries(${OCE_MODULE} ${OCE_MODEL_LIBRARIES} Python3::Module)

################
# Installation #
################
if(WIN32)
    set(EXTENSION "pyd")
else(WIN32)
    set(EXTENSION "so")
endif(WIN32)
set(BUILD_DIR ${CMAKE_BINARY_DIR}/${LIBRARY_OUTPUT_PATH})

install(FILES ${CMAKE_CURRENT_SOURCE_DIR}/src/PkgBase/__init__.py DESTINATION ${PYTHONOCC_INSTALL_DIRECTORY}/Core)
install(FILES ${CMAKE_CURRENT_SOURCE_DIR}/src/PkgBase/Exception.py DESTINATION ${PYTHONOCC_INSTALL_DIRECTORY}/Core)
# following file is necessary to mypy to use .pyi stub files
install(FILES ${CMAKE_CURRENT_SOURCE_DIR}/src/PkgBase/py.typed DESTINATION ${PYTHONOCC_INSTALL_DIRECTORY}/Core)
