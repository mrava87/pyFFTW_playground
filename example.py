# Example modified from https://github.com/keflavich/agpy/blob/master/tests/test_ffts.py
import timeit
import os
import scipy.fftpack
spfftn = scipy.fftpack.fft
spifftn = scipy.fftpack.ifft

import numpy as np
npfftn = np.fft.fft
npifftn = np.fft.ifft

import pyfftw
def wfftn(f):
    t=f()
    return t
    
def wifftn(f):
    t=f()
    return t


if __name__ == "__main__":
	print('OMP_NUM_THREADS', os.environ.get('OMP_NUM_THREADS'))
	print('MKL_NUM_THREADS', os.environ.get('MKL_NUM_THREADS'))
	
	# check results
	"""
	for dir  in ['', 'i']:
		print('Forward' if dir=='' else 'Inverse')
		for ndims in [1,2,3]:
			print("\n%i-dimensional arrays" % ndims)
			print(" ".join(["%17s" % n for n in ("n","sp","np","fftw")]))
		
			for ii in range(2, 15-ndims*2):
				
				
				array = np.random.random([2**ii]*ndims)
				outnp=npfftn(array, axis=-1)
				outsp=spfftn(array, axis=-1)

				array = array.astype('complex'); 
				outarray = array.copy();
				fft_forward = pyfftw.FFTW(array,outarray, axes=(-1,), direction='FFTW_FORWARD', flags=['FFTW_ESTIMATE'], threads=4)
				outw=wfftn(fft_forward)
				
				print(outnp-outw)
				print(outsp-outw)
	"""

	# check speed
	for dir  in ['', 'i']:
		print('Forward' if dir=='' else 'Inverse')
		for ndims in [1,2,3]:
			print("\n%i-dimensional arrays" % ndims)
			print(" ".join(["%17s" % n for n in ("n","sp","np","fftw")]))
		
			for ii in range(2, 15-ndims*2):
				
				setup="import test_ffts; import numpy as np; array = np.random.random([%i]*%i)" % (2**ii,ndims)
				setup1="import test_ffts; import numpy as np; import pyfftw;"\
					  "array = np.random.random([%i]*%i);"\
					  "array = array.astype('complex'); outarray = array.copy();"\
					  "fft_forward = pyfftw.FFTW(array,outarray, direction='FFTW_FORWARD', flags=['FFTW_ESTIMATE'], threads=4)" % (2**ii,ndims)
			
				print("%16i:" % (int(2**ii)) + \
						"".join(
							["%17f" % (min(timeit.Timer(stmt="test_ffts.%s%sfftn(array)" % (ffttype, dir), setup=setup).repeat(3,10))) for ffttype in ('sp','np')] + 
							["%17f" % (min(timeit.Timer(stmt="test_ffts.%s%sfftn(fft_forward)" % (ffttype, dir), setup=setup1).repeat(3,10))) for ffttype in ('w')]
						))
                
"""
RESULTS: (on mac book air 1.3 GHz Intel Core i5) - using np.fft.fftpack
OMP_NUM_THREADS 1
MKL_NUM_THREADS 4
Forward

1-dimensional arrays
                n                sp                np              fftw
               4:         0.000076         0.000265         0.000009
               8:         0.000060         0.000231         0.000006
              16:         0.000056         0.000275         0.000007
              32:         0.000057         0.000204         0.000007
              64:         0.000053         0.000218         0.000535
             128:         0.000058         0.000222         0.000549
             256:         0.000070         0.000248         0.000559
             512:         0.000093         0.000401         0.000524
            1024:         0.000141         0.000616         0.000566
            2048:         0.000221         0.000703         0.000639
            4096:         0.000445         0.001274         0.000832

2-dimensional arrays
                n                sp                np              fftw
               4:         0.000047         0.000236         0.000316
               8:         0.000056         0.000244         0.000292
              16:         0.000075         0.000266         0.000251
              32:         0.000144         0.000433         0.000297
              64:         0.000328         0.000768         0.000411
             128:         0.001279         0.002681         0.000675
             256:         0.005213         0.010434         0.001665
             512:         0.027889         0.076192         0.009489
            1024:         0.157087         0.381732         0.041081

3-dimensional arrays
                n                sp                np              fftw
               4:         0.000057         0.000245         0.000286
               8:         0.000119         0.000537         0.000244
              16:         0.000393         0.000663         0.000327
              32:         0.002934         0.005578         0.000769
              64:         0.046310         0.071063         0.009212
             128:         0.314014         0.648172         0.072799
             256:         3.835574         8.183702         0.540420
Inverse

1-dimensional arrays
                n                sp                np              fftw
               4:         0.000043         0.000320         0.000005
               8:         0.000045         0.000372         0.000005
              16:         0.000045         0.000316         0.000006
              32:         0.000049         0.000325         0.000007
              64:         0.000053         0.000328         0.000625
             128:         0.000059         0.000286         0.000592
             256:         0.000070         0.000334         0.000696
             512:         0.000097         0.001116         0.000466
            1024:         0.000151         0.000568         0.000696
            2048:         0.000441         0.001040         0.000657
            4096:         0.000517         0.001658         0.000939

2-dimensional arrays
                n                sp                np              fftw
               4:         0.000087         0.000524         0.000351
               8:         0.000057         0.000310         0.000305
              16:         0.000077         0.000341         0.000262
              32:         0.000288         0.000967         0.000327
              64:         0.000716         0.001345         0.000384
             128:         0.001673         0.003021         0.000818
             256:         0.005071         0.014990         0.001872
             512:         0.045723         0.107800         0.009812
            1024:         0.185921         0.522008         0.062207

3-dimensional arrays
                n                sp                np              fftw
               4:         0.000058         0.000311         0.000258
               8:         0.000202         0.000396         0.000328
              16:         0.000842         0.001375         0.000493
              32:         0.004143         0.005788         0.001213
              64:         0.040658         0.081023         0.010053
             128:         0.327148         0.786397         0.080897
             256:         3.608371        10.482571         0.584322

RESULTS: (on mac book air 1.3 GHz Intel Core i5) - using np.fft and MKL installation
OMP_NUM_THREADS 1
MKL_NUM_THREADS 4
Forward

1-dimensional arrays
                n                sp                np              fftw
               4:         0.000070         0.000041         0.000009
               8:         0.000073         0.000034         0.000006
              16:         0.000049         0.000029         0.000006
              32:         0.000052         0.000029         0.000008
              64:         0.000058         0.000033         0.000459
             128:         0.000055         0.000029         0.000582
             256:         0.000064         0.000034         0.000520
             512:         0.000089         0.000045         0.000509
            1024:         0.000135         0.000065         0.000507
            2048:         0.000405         0.000109         0.000614
            4096:         0.000440         0.000211         0.000822

2-dimensional arrays
                n                sp                np              fftw
               4:         0.000044         0.000204         0.000324
               8:         0.000053         0.000059         0.000261
              16:         0.000070         0.000074         0.000265
              32:         0.000141         0.000122         0.000271
              64:         0.000360         0.000309         0.000355
             128:         0.001424         0.001550         0.000998
             256:         0.006147         0.004437         0.002228
             512:         0.037164         0.022399         0.012736
            1024:         0.157824         0.115844         0.038376

3-dimensional arrays
                n                sp                np              fftw
               4:         0.000067         0.000059         0.000239
               8:         0.000114         0.000087         0.000264
              16:         0.000451         0.000322         0.000296
              32:         0.003196         0.002359         0.001002
              64:         0.025294         0.020147         0.008890
             128:         0.288266         0.255503         0.065049
             256:         3.762528         2.721012         0.517960
Inverse

1-dimensional arrays
                n                sp                np              fftw
               4:         0.000058         0.000031         0.000006
               8:         0.000049         0.000030         0.000006
              16:         0.000051         0.000030         0.000006
              32:         0.000043         0.000026         0.000007
              64:         0.000048         0.000029         0.000571
             128:         0.000055         0.000033         0.000588
             256:         0.000065         0.000037         0.000560
             512:         0.000092         0.000046         0.000644
            1024:         0.000147         0.000065         0.000633
            2048:         0.000253         0.000102         0.000633
            4096:         0.000509         0.000209         0.000789

2-dimensional arrays
                n                sp                np              fftw
               4:         0.000044         0.000091         0.000331
               8:         0.000100         0.000101         0.000272
              16:         0.000075         0.000077         0.000347
              32:         0.000150         0.000140         0.000286
              64:         0.000391         0.000380         0.000466
             128:         0.001503         0.001319         0.000776
             256:         0.005848         0.005016         0.002805
             512:         0.028586         0.022752         0.011378
            1024:         0.179003         0.139599         0.046708

3-dimensional arrays
                n                sp                np              fftw
               4:         0.000055         0.000066         0.000268
               8:         0.000214         0.000159         0.000307
              16:         0.000471         0.000427         0.000388
              32:         0.003443         0.002799         0.001399
              64:         0.026120         0.022912         0.010308
             128:         0.313413         0.305706         0.068711
             256:         3.646109         3.010163         0.499362
"""