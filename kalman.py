import math
import numpy as np
import numpy.linalg as linalg

class KalmanFilter():
    def __init__(self, A, B, D, R, Q):
        '''
        Initializes Kalman filter with matrices:
            x_t1_t = A*x_t_t + B*u_t
            z_t1_t = D*x_t1_t
            P_t1_t = A*P_t_t*(A^T) + Q
            S_t1 = D_t1*P_t1_t*(D_t1^T) + R
        '''
        self.A = A
        self.B = B
        self.D = D
        self.R = R
        self.Q = Q

        self.P = np.zeros(A.shape)
        self.x = np.matrix(np.zeros(A.shape[0])).transpose()

    def update(self, z, u):
        a_priori_P = self.A*self.P*self.A.transpose() + self.Q
        a_priori_S = self.D*a_priori_P*self.D.transpose() + self.R
        a_priori_x = self.A*self.x + self.B(self.x, u)
	a_priori_z = self.D*a_priori_x

        W = a_priori_P*self.D.transpose()*linalg.inv(a_priori_S)

        self.P = a_priori_P - W*a_priori_S*W.transpose()
	self.x = a_priori_x + W*(z - a_priori_z)
    def get_x(self):
        return self.x

    def get_P(self):
        return self.P

