# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_mesh_operators')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_mesh_operators')
    _mesh_operators = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_mesh_operators', [dirname(__file__)])
        except ImportError:
            import _mesh_operators
            return _mesh_operators
        try:
            _mod = imp.load_module('_mesh_operators', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _mesh_operators = swig_import_helper()
    del swig_import_helper
else:
    import _mesh_operators
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0

try:
    import weakref
    weakref_proxy = weakref.proxy
except __builtin__.Exception:
    weakref_proxy = lambda x: x


import mfem._ser.array
import mfem._ser.ostream_typemap
import mfem._ser.vector
import mfem._ser.mesh
import mfem._ser.matrix
import mfem._ser.operators
import mfem._ser.ncmesh
import mfem._ser.gridfunc
import mfem._ser.coefficient
import mfem._ser.intrules
import mfem._ser.sparsemat
import mfem._ser.densemat
import mfem._ser.eltrans
import mfem._ser.fe
import mfem._ser.fespace
import mfem._ser.fe_coll
import mfem._ser.lininteg
import mfem._ser.handle
import mfem._ser.bilininteg
import mfem._ser.linearform
import mfem._ser.element
import mfem._ser.geom
import mfem._ser.table
import mfem._ser.vertex
import mfem._ser.estimators
import mfem._ser.bilinearform
class MeshOperator(_object):
    """Proxy of C++ mfem::MeshOperator class."""

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, MeshOperator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, MeshOperator, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    NONE = _mesh_operators.MeshOperator_NONE
    CONTINUE = _mesh_operators.MeshOperator_CONTINUE
    STOP = _mesh_operators.MeshOperator_STOP
    REPEAT = _mesh_operators.MeshOperator_REPEAT
    MASK_UPDATE = _mesh_operators.MeshOperator_MASK_UPDATE
    MASK_ACTION = _mesh_operators.MeshOperator_MASK_ACTION
    REFINED = _mesh_operators.MeshOperator_REFINED
    DEREFINED = _mesh_operators.MeshOperator_DEREFINED
    REBALANCED = _mesh_operators.MeshOperator_REBALANCED
    MASK_INFO = _mesh_operators.MeshOperator_MASK_INFO

    def Apply(self, mesh):
        """Apply(MeshOperator self, Mesh mesh) -> bool"""
        return _mesh_operators.MeshOperator_Apply(self, mesh)


    def Stop(self):
        """Stop(MeshOperator self) -> bool"""
        return _mesh_operators.MeshOperator_Stop(self)


    def Repeat(self):
        """Repeat(MeshOperator self) -> bool"""
        return _mesh_operators.MeshOperator_Repeat(self)


    def Continue(self):
        """Continue(MeshOperator self) -> bool"""
        return _mesh_operators.MeshOperator_Continue(self)


    def Refined(self):
        """Refined(MeshOperator self) -> bool"""
        return _mesh_operators.MeshOperator_Refined(self)


    def Derefined(self):
        """Derefined(MeshOperator self) -> bool"""
        return _mesh_operators.MeshOperator_Derefined(self)


    def Rebalanced(self):
        """Rebalanced(MeshOperator self) -> bool"""
        return _mesh_operators.MeshOperator_Rebalanced(self)


    def GetActionInfo(self):
        """GetActionInfo(MeshOperator self) -> int"""
        return _mesh_operators.MeshOperator_GetActionInfo(self)


    def Reset(self):
        """Reset(MeshOperator self)"""
        return _mesh_operators.MeshOperator_Reset(self)

    __swig_destroy__ = _mesh_operators.delete_MeshOperator
    __del__ = lambda self: None
MeshOperator_swigregister = _mesh_operators.MeshOperator_swigregister
MeshOperator_swigregister(MeshOperator)

class MeshOperatorSequence(MeshOperator):
    """Proxy of C++ mfem::MeshOperatorSequence class."""

    __swig_setmethods__ = {}
    for _s in [MeshOperator]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, MeshOperatorSequence, name, value)
    __swig_getmethods__ = {}
    for _s in [MeshOperator]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, MeshOperatorSequence, name)
    __repr__ = _swig_repr

    def __init__(self):
        """__init__(mfem::MeshOperatorSequence self) -> MeshOperatorSequence"""
        this = _mesh_operators.new_MeshOperatorSequence()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _mesh_operators.delete_MeshOperatorSequence
    __del__ = lambda self: None

    def Append(self, mc):
        """Append(MeshOperatorSequence self, MeshOperator mc)"""
        return _mesh_operators.MeshOperatorSequence_Append(self, mc)


    def GetSequence(self):
        """GetSequence(MeshOperatorSequence self) -> mfem::Array< mfem::MeshOperator * > &"""
        return _mesh_operators.MeshOperatorSequence_GetSequence(self)


    def Reset(self):
        """Reset(MeshOperatorSequence self)"""
        return _mesh_operators.MeshOperatorSequence_Reset(self)

MeshOperatorSequence_swigregister = _mesh_operators.MeshOperatorSequence_swigregister
MeshOperatorSequence_swigregister(MeshOperatorSequence)

class ThresholdRefiner(MeshOperator):
    """Proxy of C++ mfem::ThresholdRefiner class."""

    __swig_setmethods__ = {}
    for _s in [MeshOperator]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, ThresholdRefiner, name, value)
    __swig_getmethods__ = {}
    for _s in [MeshOperator]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, ThresholdRefiner, name)
    __repr__ = _swig_repr

    def __init__(self, est):
        """__init__(mfem::ThresholdRefiner self, ErrorEstimator est) -> ThresholdRefiner"""
        this = _mesh_operators.new_ThresholdRefiner(est)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def SetTotalErrorNormP(self, *args):
        """
        SetTotalErrorNormP(ThresholdRefiner self, double norm_p)
        SetTotalErrorNormP(ThresholdRefiner self)
        """
        return _mesh_operators.ThresholdRefiner_SetTotalErrorNormP(self, *args)


    def SetTotalErrorGoal(self, err_goal):
        """SetTotalErrorGoal(ThresholdRefiner self, double err_goal)"""
        return _mesh_operators.ThresholdRefiner_SetTotalErrorGoal(self, err_goal)


    def SetTotalErrorFraction(self, fraction):
        """SetTotalErrorFraction(ThresholdRefiner self, double fraction)"""
        return _mesh_operators.ThresholdRefiner_SetTotalErrorFraction(self, fraction)


    def SetLocalErrorGoal(self, err_goal):
        """SetLocalErrorGoal(ThresholdRefiner self, double err_goal)"""
        return _mesh_operators.ThresholdRefiner_SetLocalErrorGoal(self, err_goal)


    def SetMaxElements(self, max_elem):
        """SetMaxElements(ThresholdRefiner self, long max_elem)"""
        return _mesh_operators.ThresholdRefiner_SetMaxElements(self, max_elem)


    def PreferNonconformingRefinement(self):
        """PreferNonconformingRefinement(ThresholdRefiner self)"""
        return _mesh_operators.ThresholdRefiner_PreferNonconformingRefinement(self)


    def PreferConformingRefinement(self):
        """PreferConformingRefinement(ThresholdRefiner self)"""
        return _mesh_operators.ThresholdRefiner_PreferConformingRefinement(self)


    def SetNCLimit(self, nc_limit):
        """SetNCLimit(ThresholdRefiner self, int nc_limit)"""
        return _mesh_operators.ThresholdRefiner_SetNCLimit(self, nc_limit)


    def GetNumMarkedElements(self):
        """GetNumMarkedElements(ThresholdRefiner self) -> long"""
        return _mesh_operators.ThresholdRefiner_GetNumMarkedElements(self)


    def GetThreshold(self):
        """GetThreshold(ThresholdRefiner self) -> double"""
        return _mesh_operators.ThresholdRefiner_GetThreshold(self)


    def Reset(self):
        """Reset(ThresholdRefiner self)"""
        return _mesh_operators.ThresholdRefiner_Reset(self)

    __swig_destroy__ = _mesh_operators.delete_ThresholdRefiner
    __del__ = lambda self: None
ThresholdRefiner_swigregister = _mesh_operators.ThresholdRefiner_swigregister
ThresholdRefiner_swigregister(ThresholdRefiner)

class ThresholdDerefiner(MeshOperator):
    """Proxy of C++ mfem::ThresholdDerefiner class."""

    __swig_setmethods__ = {}
    for _s in [MeshOperator]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, ThresholdDerefiner, name, value)
    __swig_getmethods__ = {}
    for _s in [MeshOperator]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, ThresholdDerefiner, name)
    __repr__ = _swig_repr

    def __init__(self, est):
        """__init__(mfem::ThresholdDerefiner self, ErrorEstimator est) -> ThresholdDerefiner"""
        this = _mesh_operators.new_ThresholdDerefiner(est)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def SetThreshold(self, thresh):
        """SetThreshold(ThresholdDerefiner self, double thresh)"""
        return _mesh_operators.ThresholdDerefiner_SetThreshold(self, thresh)


    def SetOp(self, op):
        """SetOp(ThresholdDerefiner self, int op)"""
        return _mesh_operators.ThresholdDerefiner_SetOp(self, op)


    def SetNCLimit(self, nc_limit):
        """SetNCLimit(ThresholdDerefiner self, int nc_limit)"""
        return _mesh_operators.ThresholdDerefiner_SetNCLimit(self, nc_limit)


    def Reset(self):
        """Reset(ThresholdDerefiner self)"""
        return _mesh_operators.ThresholdDerefiner_Reset(self)

    __swig_destroy__ = _mesh_operators.delete_ThresholdDerefiner
    __del__ = lambda self: None
ThresholdDerefiner_swigregister = _mesh_operators.ThresholdDerefiner_swigregister
ThresholdDerefiner_swigregister(ThresholdDerefiner)

class Rebalancer(MeshOperator):
    """Proxy of C++ mfem::Rebalancer class."""

    __swig_setmethods__ = {}
    for _s in [MeshOperator]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, Rebalancer, name, value)
    __swig_getmethods__ = {}
    for _s in [MeshOperator]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, Rebalancer, name)
    __repr__ = _swig_repr

    def Reset(self):
        """Reset(Rebalancer self)"""
        return _mesh_operators.Rebalancer_Reset(self)


    def __init__(self):
        """__init__(mfem::Rebalancer self) -> Rebalancer"""
        this = _mesh_operators.new_Rebalancer()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _mesh_operators.delete_Rebalancer
    __del__ = lambda self: None
Rebalancer_swigregister = _mesh_operators.Rebalancer_swigregister
Rebalancer_swigregister(Rebalancer)

# This file is compatible with both classic and new-style classes.

