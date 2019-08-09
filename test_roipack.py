import matplotlib; matplotlib.use('Agg')
import cortex
import cortex.rois
import nibabel as nib
import os

# load glasser atlas
lh_aparc_file = os.path.join('atlases','lh.HCP-MMP1.annot')
rh_aparc_file = os.path.join('atlases','rh.HCP-MMP1.annot')
lpinds, lpstats, lpnames = nib.freesurfer.read_annot(lh_aparc_file)
lpinds_orig, lpstats, lpnames = nib.freesurfer.read_annot(lh_aparc_file, True)
lpinds[lpinds_orig==0] = -1
rpinds, rpstats, rpnames = nib.freesurfer.read_annot(rh_aparc_file)
rpinds_orig, rpstats, rpnames = nib.freesurfer.read_annot(rh_aparc_file, True)
rpinds[rpinds_orig==0] = -1


# create roipack object
roipack = cortex.rois.ROIpack('fsaverage_pycortex', 'blah')

# create vertexdata for an roi
vd = cortex.Vertex(lpinds == 12, 'fsaverage_pycortex')

# jam it into the roipack
roipack.rois['test'] = vd

# save the dang thing out as an svg file
roipack.to_svg(filename='test.svg')
