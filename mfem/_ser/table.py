# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _table
else:
    import _table

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _table.SWIG_PyInstanceMethod_New
_swig_new_static_method = _table.SWIG_PyStaticMethod_New

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


import mfem._ser.array
import mfem._ser.mem_manager
class Connection(object):
    r"""Proxy of C++ mfem::Connection class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    _from = property(_table.Connection__from_get, _table.Connection__from_set, doc=r"""_from : int""")
    to = property(_table.Connection_to_get, _table.Connection_to_set, doc=r"""to : int""")

    def __init__(self, *args):
        r"""
        __init__(Connection self) -> Connection
        __init__(Connection self, int _from, int to) -> Connection
        """
        _table.Connection_swiginit(self, _table.new_Connection(*args))

    def __eq__(self, rhs):
        r"""__eq__(Connection self, Connection rhs) -> bool"""
        return _table.Connection___eq__(self, rhs)
    __eq__ = _swig_new_instance_method(_table.Connection___eq__)

    def __lt__(self, rhs):
        r"""__lt__(Connection self, Connection rhs) -> bool"""
        return _table.Connection___lt__(self, rhs)
    __lt__ = _swig_new_instance_method(_table.Connection___lt__)
    __swig_destroy__ = _table.delete_Connection

# Register Connection in _table:
_table.Connection_swigregister(Connection)

class Table(object):
    r"""Proxy of C++ mfem::Table class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(Table self) -> Table
        __init__(Table self, Table arg2) -> Table
        __init__(Table self, int dim, int connections_per_row=3) -> Table
        __init__(Table self, int nrows, mfem::Array< mfem::Connection > & list) -> Table
        __init__(Table self, int nrows, int * partitioning) -> Table
        """
        _table.Table_swiginit(self, _table.new_Table(*args))

    def MakeI(self, nrows):
        r"""MakeI(Table self, int nrows)"""
        return _table.Table_MakeI(self, nrows)
    MakeI = _swig_new_instance_method(_table.Table_MakeI)

    def AddAColumnInRow(self, r):
        r"""AddAColumnInRow(Table self, int r)"""
        return _table.Table_AddAColumnInRow(self, r)
    AddAColumnInRow = _swig_new_instance_method(_table.Table_AddAColumnInRow)

    def AddColumnsInRow(self, r, ncol):
        r"""AddColumnsInRow(Table self, int r, int ncol)"""
        return _table.Table_AddColumnsInRow(self, r, ncol)
    AddColumnsInRow = _swig_new_instance_method(_table.Table_AddColumnsInRow)

    def MakeJ(self):
        r"""MakeJ(Table self)"""
        return _table.Table_MakeJ(self)
    MakeJ = _swig_new_instance_method(_table.Table_MakeJ)

    def AddConnection(self, r, c):
        r"""AddConnection(Table self, int r, int c)"""
        return _table.Table_AddConnection(self, r, c)
    AddConnection = _swig_new_instance_method(_table.Table_AddConnection)

    def AddConnections(self, r, c, nc):
        r"""AddConnections(Table self, int r, int const * c, int nc)"""
        return _table.Table_AddConnections(self, r, c, nc)
    AddConnections = _swig_new_instance_method(_table.Table_AddConnections)

    def ShiftUpI(self):
        r"""ShiftUpI(Table self)"""
        return _table.Table_ShiftUpI(self)
    ShiftUpI = _swig_new_instance_method(_table.Table_ShiftUpI)

    def SetSize(self, dim, connections_per_row):
        r"""SetSize(Table self, int dim, int connections_per_row)"""
        return _table.Table_SetSize(self, dim, connections_per_row)
    SetSize = _swig_new_instance_method(_table.Table_SetSize)

    def SetDims(self, rows, nnz):
        r"""SetDims(Table self, int rows, int nnz)"""
        return _table.Table_SetDims(self, rows, nnz)
    SetDims = _swig_new_instance_method(_table.Table_SetDims)

    def Size(self):
        r"""Size(Table self) -> int"""
        return _table.Table_Size(self)
    Size = _swig_new_instance_method(_table.Table_Size)

    def Size_of_connections(self):
        r"""Size_of_connections(Table self) -> int"""
        return _table.Table_Size_of_connections(self)
    Size_of_connections = _swig_new_instance_method(_table.Table_Size_of_connections)

    def __call__(self, i, j):
        r"""__call__(Table self, int i, int j) -> int"""
        return _table.Table___call__(self, i, j)
    __call__ = _swig_new_instance_method(_table.Table___call__)

    def RowSize(self, i):
        r"""RowSize(Table self, int i) -> int"""
        return _table.Table_RowSize(self, i)
    RowSize = _swig_new_instance_method(_table.Table_RowSize)

    def GetRow(self, *args):
        r"""
        GetRow(Table self, int i, intArray row)
        GetRow(Table self, int i) -> int const
        GetRow(Table self, int i) -> int *
        """
        return _table.Table_GetRow(self, *args)
    GetRow = _swig_new_instance_method(_table.Table_GetRow)

    def GetI(self, *args):
        r"""
        GetI(Table self) -> int
        GetI(Table self) -> int const *
        """
        return _table.Table_GetI(self, *args)
    GetI = _swig_new_instance_method(_table.Table_GetI)

    def GetJ(self, *args):
        r"""
        GetJ(Table self) -> int
        GetJ(Table self) -> int const *
        """
        return _table.Table_GetJ(self, *args)
    GetJ = _swig_new_instance_method(_table.Table_GetJ)

    def GetIMemory(self, *args):
        r"""
        GetIMemory(Table self) -> mfem::Memory< int >
        GetIMemory(Table self) -> mfem::Memory< int > const &
        """
        return _table.Table_GetIMemory(self, *args)
    GetIMemory = _swig_new_instance_method(_table.Table_GetIMemory)

    def GetJMemory(self, *args):
        r"""
        GetJMemory(Table self) -> mfem::Memory< int >
        GetJMemory(Table self) -> mfem::Memory< int > const &
        """
        return _table.Table_GetJMemory(self, *args)
    GetJMemory = _swig_new_instance_method(_table.Table_GetJMemory)

    def SortRows(self):
        r"""SortRows(Table self)"""
        return _table.Table_SortRows(self)
    SortRows = _swig_new_instance_method(_table.Table_SortRows)

    def SetIJ(self, newI, newJ, newsize=-1):
        r"""SetIJ(Table self, int * newI, int * newJ, int newsize=-1)"""
        return _table.Table_SetIJ(self, newI, newJ, newsize)
    SetIJ = _swig_new_instance_method(_table.Table_SetIJ)

    def Push(self, i, j):
        r"""Push(Table self, int i, int j) -> int"""
        return _table.Table_Push(self, i, j)
    Push = _swig_new_instance_method(_table.Table_Push)

    def Finalize(self):
        r"""Finalize(Table self)"""
        return _table.Table_Finalize(self)
    Finalize = _swig_new_instance_method(_table.Table_Finalize)

    def MakeFromList(self, nrows, list):
        r"""MakeFromList(Table self, int nrows, mfem::Array< mfem::Connection > const & list)"""
        return _table.Table_MakeFromList(self, nrows, list)
    MakeFromList = _swig_new_instance_method(_table.Table_MakeFromList)

    def Width(self):
        r"""Width(Table self) -> int"""
        return _table.Table_Width(self)
    Width = _swig_new_instance_method(_table.Table_Width)

    def LoseData(self):
        r"""LoseData(Table self)"""
        return _table.Table_LoseData(self)
    LoseData = _swig_new_instance_method(_table.Table_LoseData)

    def Load(self, _in):
        r"""Load(Table self, std::istream & _in)"""
        return _table.Table_Load(self, _in)
    Load = _swig_new_instance_method(_table.Table_Load)

    def Copy(self, copy):
        r"""Copy(Table self, Table copy)"""
        return _table.Table_Copy(self, copy)
    Copy = _swig_new_instance_method(_table.Table_Copy)

    def Swap(self, other):
        r"""Swap(Table self, Table other)"""
        return _table.Table_Swap(self, other)
    Swap = _swig_new_instance_method(_table.Table_Swap)

    def Clear(self):
        r"""Clear(Table self)"""
        return _table.Table_Clear(self)
    Clear = _swig_new_instance_method(_table.Table_Clear)

    def MemoryUsage(self):
        r"""MemoryUsage(Table self) -> long"""
        return _table.Table_MemoryUsage(self)
    MemoryUsage = _swig_new_instance_method(_table.Table_MemoryUsage)
    __swig_destroy__ = _table.delete_Table

    def GetRowList(self, i):
        r"""GetRowList(Table self, int i) -> PyObject *"""
        return _table.Table_GetRowList(self, i)
    GetRowList = _swig_new_instance_method(_table.Table_GetRowList)

    def Print(self, *args):
        r"""
        Print(Table self, std::ostream & out=mfem::out, int width=4)
        Print(Table self, char const * file, int precision=16)
        """
        return _table.Table_Print(self, *args)
    Print = _swig_new_instance_method(_table.Table_Print)

    def PrintGZ(self, file, precision=16):
        r"""PrintGZ(Table self, char const * file, int precision=16)"""
        return _table.Table_PrintGZ(self, file, precision)
    PrintGZ = _swig_new_instance_method(_table.Table_PrintGZ)

    def PrintMatlab(self, *args):
        r"""
        PrintMatlab(Table self, std::ostream & out)
        PrintMatlab(Table self, char const * file, int precision=16)
        """
        return _table.Table_PrintMatlab(self, *args)
    PrintMatlab = _swig_new_instance_method(_table.Table_PrintMatlab)

    def PrintMatlabGZ(self, file, precision=16):
        r"""PrintMatlabGZ(Table self, char const * file, int precision=16)"""
        return _table.Table_PrintMatlabGZ(self, file, precision)
    PrintMatlabGZ = _swig_new_instance_method(_table.Table_PrintMatlabGZ)

    def SaveGZ(self, file, precision=16):
        r"""SaveGZ(Table self, char const * file, int precision=16)"""
        return _table.Table_SaveGZ(self, file, precision)
    SaveGZ = _swig_new_instance_method(_table.Table_SaveGZ)

    def Save(self, *args):
        r"""
        Save(Table self, std::ostream & out)
        Save(Table self, char const * file, int precision=16)
        Save(Table self)
        """
        return _table.Table_Save(self, *args)
    Save = _swig_new_instance_method(_table.Table_Save)

# Register Table in _table:
_table.Table_swigregister(Table)

class STable(Table):
    r"""Proxy of C++ mfem::STable class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, dim, connections_per_row=3):
        r"""__init__(STable self, int dim, int connections_per_row=3) -> STable"""
        _table.STable_swiginit(self, _table.new_STable(dim, connections_per_row))

    def __call__(self, i, j):
        r"""__call__(STable self, int i, int j) -> int"""
        return _table.STable___call__(self, i, j)
    __call__ = _swig_new_instance_method(_table.STable___call__)

    def Push(self, i, j):
        r"""Push(STable self, int i, int j) -> int"""
        return _table.STable_Push(self, i, j)
    Push = _swig_new_instance_method(_table.STable_Push)
    __swig_destroy__ = _table.delete_STable

# Register STable in _table:
_table.STable_swigregister(STable)

class DSTable(object):
    r"""Proxy of C++ mfem::DSTable class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, nrows):
        r"""__init__(DSTable self, int nrows) -> DSTable"""
        _table.DSTable_swiginit(self, _table.new_DSTable(nrows))

    def NumberOfRows(self):
        r"""NumberOfRows(DSTable self) -> int"""
        return _table.DSTable_NumberOfRows(self)
    NumberOfRows = _swig_new_instance_method(_table.DSTable_NumberOfRows)

    def NumberOfEntries(self):
        r"""NumberOfEntries(DSTable self) -> int"""
        return _table.DSTable_NumberOfEntries(self)
    NumberOfEntries = _swig_new_instance_method(_table.DSTable_NumberOfEntries)

    def Push(self, a, b):
        r"""Push(DSTable self, int a, int b) -> int"""
        return _table.DSTable_Push(self, a, b)
    Push = _swig_new_instance_method(_table.DSTable_Push)

    def __call__(self, a, b):
        r"""__call__(DSTable self, int a, int b) -> int"""
        return _table.DSTable___call__(self, a, b)
    __call__ = _swig_new_instance_method(_table.DSTable___call__)
    __swig_destroy__ = _table.delete_DSTable

# Register DSTable in _table:
_table.DSTable_swigregister(DSTable)



