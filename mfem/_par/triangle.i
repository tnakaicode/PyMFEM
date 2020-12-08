%module(package="mfem._par") triangle
%{
#include  "mfem.hpp"
#include "mesh/triangle.hpp"
#include "numpy/arrayobject.h"    
%}

%init %{
import_array();
%}
%include "exception.i"
%import "fe.i"
%import "element.i"
%include "../common/typemap_macros.i"
%include "../common/exception.i"

LIST_TO_INTARRAY_IN(const int *ind, 2)
INTARRAY_OUT_TO_TUPLE(int *GetVertices, 2)

%include "../common/deprecation.i"
DEPRECATED_OVERLOADED_METHOD(mfem::Triangle::GetNFaces,
    	                     Triangle::GetNFaces(int & nFaceVertices) is deprecated,
			     len(args) == 1)

%include "mesh/triangle.hpp"
