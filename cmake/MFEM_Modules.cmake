LIST(APPEND MFEM_COMMON
	array_instantiation_macro
	array_listtuple_typemap
	bilininteg_ext
	coefficient_common
	complex_fem_ext
	const_doubleptr_typemap
	const_intptr_typemap
	cpointers
	data_size_typemap
	deprecation
	enum_class
	exception
	exception_director
	handle_template
	hypre_int
	ignore_common_functions
	io_stream_typemap
	lininteg_ext
	memorytype_typemap
#	mfem_config
#	numba_coefficient
	numpy_int_typemap
	object_array_typemap
	operator_ptr_typemap
	typemap_macros
)

LIST(APPEND MFEM_SER
	array
	bilinearform
	bilininteg
	blockmatrix
	blockoperator
	blockvector
	coefficient
	common_functions
	complex_fem
	complex_operator
	constraints
	cpointers
	datacollection
	densemat
	device
	doftrans
	element
	eltrans
	error
	estimators
	fe
	fespace
	fespacehierarchy
	fe_base
	fe_coll
	fe_fixed_order
	fe_h1
	fe_l2
	fe_nd
	fe_nurbs
	fe_pos
	fe_rt
	fe_ser
	geom
	globals
	gridfunc
	gslib
	handle
	hash
	hexahedron
	hybridization
	intrules
	io_stream
	istream_typemap
	linearform
	lininteg
	matrix
	mem_manager
	mesh
	mesh_operators
	multigrid
	ncmesh
	nonlinearform
	nonlininteg
	ode
	operators
	ostream_typemap
	point
	qfunction
	qspace
	quadinterpolator
	quadinterpolator_face
	quadrilateral
	restriction
	segment
	sets
	socketstream
	solvers
	sort_pairs
	sparsemat
	sparsesmoothers
	stable3d
	std_vectors
	submesh
	symmat
	table
	tetrahedron
	tmop
	tmop_amr
	tmop_tools
	transfer
	transfermap
	triangle
	vector
	vertex
	vtk
	wedge
)

LIST(APPEND MFEM_PAR
	array
	auxiliary
	bilinearform
	bilininteg
	blockmatrix
	blockoperator
	blockvector
	coefficient
	common_functions
	communication
	complex_fem
	complex_operator
	constraints
	cpointers
	datacollection
	densemat
	device
	dist_solver
	doftrans
	element
	eltrans
	error
	estimators
	fe
	fespace
	fespacehierarchy
	fe_base
	fe_coll
	fe_fixed_order
	fe_h1
	fe_l2
	fe_nd
	fe_nurbs
	fe_pos
	fe_rt
	fe_ser
	geom
	globals
	gridfunc
	gslib
	handle
	hash
	hexahedron
	hybridization
	hypre
	intrules
	io_stream
	istream_typemap
	linearform
	lininteg
	matrix
	mem_manager
	mesh
	mesh_operators
	multigrid
	ncmesh
	nonlinearform
	nonlininteg
	ode
	operators
	ostream_typemap
	pbilinearform
	pfespace
	pgridfunc
	plinearform
	pmesh
	pncmesh
	pnonlinearform
	point
	prestriction
	psubmesh
	ptransfermap
	pumi
	qfunction
	qspace
	quadinterpolator
	quadinterpolator_face
	quadrilateral
	restriction
	schwarz
	segment
	sets
	socketstream
	solvers
	sort_pairs
	sparsemat
	sparsesmoothers
	stable3d
	std_vectors
	strumpack
	submesh
	symmat
	table
	tetrahedron
	tmop
	tmop_amr
	tmop_tools
	transfer
	transfermap
	triangle
	vector
	vertex
	vtk
	wedge
)
