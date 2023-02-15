cmake_minimum_required(VERSION 3.0.0)
project(PyMFEM VERSION 0.1.0)

include(CTest)
enable_testing()

set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
include(CPack)

########
# SWIG #
########
find_package(SWIG 4.0.2 REQUIRED)
include(${SWIG_USE_FILE})
set(SWIG_FILES_PATH src/SWIG_files/wrapper)
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
    message(STATUS "MFEM binary directory: " ${MFEM_BINARY_DIR})
    include_directories(${MFEM_INCLUDE_DIR})
  else(MFEM_FOUND)  # set default paths
    set(MFEM_INCLUDE_PATH /usr/local/include/MFEM CACHE PATH "MFEM include path")
    set(MFEM_LIB_PATH /usr/local/lib CACHE PATH "MFEM lib path")
    include_directories(${MFEM_INCLUDE_PATH})
    link_directories(${MFEM_LIB_PATH})
  endif(MFEM_FOUND)
endif(DEFINED MFEM_INCLUDE_PATH)
