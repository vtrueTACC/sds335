import os
import sys
try: paraview.simple
except: from paraview.simple import *
paraview.simple._DisableFirstRenderCameraReset()

# WHIPple ITeration script 

AnimationScene1 = GetAnimationScene()
timesteps = []
def svbSetup(geometryLevel=1,stage=0):
	""" Specify the dataset here. Check to see if it exists
	 (these things have a way of changing places) Check to
	 see if we have access and open it with the Exodus 
	 reader if we do. 
	
	 If all is well do the initial file open read and setup. 
	 All the svbSetup should do is set the AnimationTime 
	 that corresponds to the particular stage/timestep and render
	"""
	print "CALL svbSETUP"
	datasetpath = '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.000'
	if os.path.exists(datasetpath):
		if os.access(datasetpath,os.R_OK):
			Whipple_Shield_exo_300_010 = ExodusIIReader(FileName=[datasetpath])
		else:
			print "Read Permission Denied for: %s\n" % datasetpath
			sys.exit()
	else:
		print "Dataset %s does not exist\n" % datasetpath
		sys.exit()

	global AnimationScene1 
	global timesteps
	if stage == 0: #pipeline setup
		timesteps = Whipple_Shield_exo_300_010.TimestepValues
		AnimationScene1.EndTime = timesteps[len(timesteps)-1]
		AnimationScene1.PlayMode = 'Snap To TimeSteps'

		Whipple_Shield_exo_300_010.FileRange = [0, 299]
		Whipple_Shield_exo_300_010.XMLFileName = 'Invalid result'
		Whipple_Shield_exo_300_010.FilePrefix = '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.'
		Whipple_Shield_exo_300_010.ModeShape = 20
		Whipple_Shield_exo_300_010.FilePattern = '%s%03i'


#		RenderView1 = GetRenderView()
#		RenderView1.CenterOfRotation = [0.0, 0.0, 0.018435800448060036]

		Whipple_Shield_exo_300_010.NodeSetArrayStatus = []
		Whipple_Shield_exo_300_010.ElementVariables = ['VOID_FRC', 'VOLFRC1', 'VOLFRC2', 'DENSITY']
		Whipple_Shield_exo_300_010.ElementBlocks = ['Unnamed block ID: 1 Type: HEX']

#		DataRepresentation1 = Show()
#		DataRepresentation1.EdgeColor = [0.0, 0.0, 0.5000076295109483]
#		DataRepresentation1.SelectionPointFieldDataArrayName = 'GlobalNodeId'
#		DataRepresentation1.SelectionCellFieldDataArrayName = 'DENSITY'
#		DataRepresentation1.ScalarOpacityUnitDistance = 0.0002821527718911672
#		DataRepresentation1.ExtractedBlockIndex = 2
#		DataRepresentation1.ScaleFactor = 0.005079999938607216

#		RenderView1.CameraPosition = [0.0, 0.0, 0.18813575352296963]
#		RenderView1.CameraFocalPoint = [0.0, 0.0, 0.018435800448060036]
#		RenderView1.CameraClippingRange = [0.11770729481791534, 0.23555732428522624]
#		RenderView1.CameraParallelScale = 0.043921579808790676

		CellDatatoPointData1 = CellDatatoPointData()

#		DataRepresentation2 = Show()
#		DataRepresentation2.EdgeColor = [0.0, 0.0, 0.5000076295109483]
#		DataRepresentation2.SelectionPointFieldDataArrayName = 'DENSITY'
#		DataRepresentation2.SelectionCellFieldDataArrayName = 'DENSITY'
#		DataRepresentation2.ScalarOpacityUnitDistance = 0.0002821527718911672
#		DataRepresentation2.ExtractedBlockIndex = 2
#		DataRepresentation2.ScaleFactor = 0.005079999938607216

#		DataRepresentation1.Visibility = 0

		Contour1 = Contour( PointMergeMethod="Uniform Binning" )

		Contour1.PointMergeMethod = "Uniform Binning"
		Contour1.ContourBy = ['POINTS', 'DENSITY']
		Contour1.Isosurfaces = [3943.054656982422]

		Contour1.Isosurfaces = [0.5]
		Contour1.ContourBy = ['POINTS', 'VOLFRC2']

		DataRepresentation3 = Show()
		DataRepresentation3.ScaleFactor = 0.005079999938607216
		DataRepresentation3.EdgeColor = [0.0, 0.0, 0.5000076295109483]
		DataRepresentation3.SelectionPointFieldDataArrayName = 'DENSITY'
		DataRepresentation3.SelectionCellFieldDataArrayName = 'DENSITY'

		SetActiveSource(CellDatatoPointData1)

		Contour2 = Contour( PointMergeMethod="Uniform Binning" )

                Contour2.PointMergeMethod = "Uniform Binning"
                Contour2.ContourBy = ['POINTS', 'DENSITY']
                Contour2.Isosurfaces = [3943.054656982422]

                Contour2.Isosurfaces = [0.5]
                Contour2.ContourBy = ['POINTS', 'VOLFRC1']

		DataRepresentation4 = Show()
		DataRepresentation4.ScaleFactor = 0.005079999938607216
		DataRepresentation4.EdgeColor = [0.0, 0.0, 0.5000076295109483]
		DataRepresentation4.SelectionPointFieldDataArrayName = 'DENSITY'
		DataRepresentation4.SelectionCellFieldDataArrayName = 'DENSITY'
#		DataRepresentation2.Visibility = 0

	AnimationScene1.AnimationTime = timesteps[stage]
	RenderView1 = GetRenderView()
	RenderView1.CenterOfRotation = [0.0, 0.0, 0.018435800448060036]
	RenderView1.CameraViewUp = [-0.041981806193924054, -0.6484761172246292, -0.7600764786111757]
	RenderView1.CameraPosition = [-0.012931246084195372, 0.05071249414152018, -0.04261877853747655]
	RenderView1.CameraClippingRange = [0.007083748934846819, 0.1534122165178119]
	RenderView1.CameraFocalPoint = [0.0006400393297762241, -0.008990028403178798, 0.0075681618661409275]
	RenderView1.CameraParallelScale = 0.043921579808790676


# this function returns the number of time steps.
# Stages are used for time steps in this script. 
# The svbSetup function uses the stage to indicate
# what timestep to render. 
def svbGetStagesSize():
	global timesteps
	return 2
	#uncomment next line to do the whole time series
	#return len(timesteps);

#def svbSetup(geometryLevel=1, stage=0):
#	global AnimationScene1
#	global timesteps
#	AnimationScene1.AnimationTime = timesteps[stage]
#	Render()
def svbRender():
	Render()
