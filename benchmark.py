# Benchmark performance (modified from https://github.com/keflavich/agpy/blob/master/tests/test_ffts.py)
#
# Usage: python performance.py computer fft 10
#
# where you can specify your computer (eg mac_book_air_1_3_GHz_Intel_Core_i5), if you want to use
# np.fft or fftpack (the first using MKL if installed with conda, the second being the slower if MKL
# is not available), and the number of times an fft is tested by timeit function (>10 to be somehow
# reliable)
#
# Author: Matteo Ravasi
#
########################################################################################################
import sys
import timeit
import os
import matplotlib.pyplot as plt
import scipy.fftpack
spfftn = scipy.fftpack.fft
spifftn = scipy.fftpack.ifft

import numpy as np
if sys.argv[2]=='fft':
	print('use np.fft')
	nplabel='np_fft'
	npfftn = np.fft.fft
	npifftn = np.fft.ifft
elif sys.argv[2]=='fftpack':
	print('use np.fft.fftpack')
	nplabel='np_fftpack'
	npfftn = np.fft.fftpack.fft
	npifftn = np.fft.fftpack.ifft

import pyfftw
def wfftn(f):
    t=f()
    return t
    
def wifftn(f):
    t=f()
    return t

directions_np = {'':npfftn, 'i':npifftn}
directions_sp = {'':spfftn, 'i':spifftn}
directions_fftw = {'':'FFTW_FORWARD', 'i':'FFTW_BACKWARD'}

if __name__ == "__main__":
	print('OMP_NUM_THREADS', os.environ.get('OMP_NUM_THREADS'))
	print('MKL_NUM_THREADS', os.environ.get('MKL_NUM_THREADS'))

	# check obtain same results
	for dir  in ['', 'i']:
		print('Forward' if dir=='' else 'Inverse')
		for ndims in [1,2,3]:
			for ii in range(2, 15 - ndims * 2):
				array = np.random.random([2**ii]*ndims)
				outnp=directions_np[dir](array, axis=-1)
				outsp=directions_sp[dir](array, axis=-1)

				array = array.astype('complex'); 
				outarray = array.copy();
				fft_forward = pyfftw.FFTW(array,outarray, axes=(-1,), direction=directions_fftw[dir], flags=['FFTW_ESTIMATE'], threads=int(os.environ.get('OMP_NUM_THREADS')))
				outw=wfftn(fft_forward)

				#print("\n%i-dimensional arrays" % ndims)
				#print('np-fftw',np.linalg.norm(outnp-outw))
				#print('sp-fftw',np.linalg.norm(outsp-outw))
				if np.linalg.norm(outnp-outw)>1e-10 or np.linalg.norm(outsp-outw)>1e-10:
					raise ValueError('np-sp-fftw do not give same results for %s %d dim % ii size' %(dir, ndims, ii))

	# compare speed
	fig, axs = plt.subplots(3, 1, figsize=(15, 12))
	fig.suptitle(sys.argv[1]+'(OMP_NUM_THREADS=%s, MKL_NUM_THREADS=%s)'
				 %(os.environ.get('OMP_NUM_THREADS'), os.environ.get('MKL_NUM_THREADS')))
	axs[0].set_title('1d signal')
	axs[1].set_title('2d signal')
	axs[2].set_title('3d signal')
	for dir  in ['', 'i']:
		print('Forward' if dir=='' else 'Inverse')
		for ndims in [1,2,3]:
			print("\n%i-dimensional arrays" % ndims)
			print(" ".join(["%17s" % n for n in ("n","sp","np","fftw")]))
			sizes = range(2, 15 - ndims * 2)
			np_speed = np.zeros(len(sizes))
			sp_speed = np.zeros(len(sizes))
			fftw_speed = np.zeros(len(sizes))
			for i, ii in enumerate(sizes):
				setup="import benchmark; import numpy as np; array = np.random.random([%i]*%i)" % (2**ii,ndims)
				setup1="import benchmark; import numpy as np; import pyfftw;"\
					  "array = np.random.random([%i]*%i);"\
					  "array = array.astype('complex'); outarray = array.copy();"\
					  "fft_forward = pyfftw.FFTW(array,outarray, direction='%s', flags=['FFTW_ESTIMATE'], threads=%d)" % (2**ii, ndims, directions_fftw[dir], int(os.environ.get('OMP_NUM_THREADS')))
				tnp = min(timeit.Timer(stmt="benchmark.%s%sfftn(array)" % ('np', dir), setup=setup).repeat(3,int(sys.argv[3])))
				tsp = min(timeit.Timer(stmt="benchmark.%s%sfftn(array)" % ('sp', dir), setup=setup).repeat(3, int(sys.argv[3])))
				tfftw = min(timeit.Timer(stmt="benchmark.%s%sfftn(fft_forward)" % ('w', dir), setup=setup1).repeat(3, int(sys.argv[3])))
				np_speed[i] = tnp
				sp_speed[i] = tsp
				fftw_speed[i] = tfftw
				print("%16i:" % (int(2**ii)) + \
						"".join(["%17f" % (i) for i in [tsp, tnp, tfftw]]))
			axs[ndims-1].semilogy(np_speed, 'r' if dir=='' else '--r', label=nplabel if dir=='' else nplabel+'-inv')
			axs[ndims-1].semilogy(sp_speed, 'g' if dir=='' else '--g', label='sp' if dir=='' else 'sp-inv')
			axs[ndims-1].semilogy(fftw_speed, 'b' if dir=='' else '--b', label='fftw' if dir=='' else 'fftw-inv')
	axs[0].legend(loc=2)
	plt.savefig(os.path.join('benchmarks', sys.argv[1]+'__'+nplabel+'.png'), dpi=300)
	plt.show()

