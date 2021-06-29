def gibbs_sampler(ini_point,sample_no=3):
    point=ini_point
    for i in range(sample_no):
        point_1=sigmoid(point.dot(self.W)+self.h)
        point=sigmoid(point1.dot(self.W.T) + self.b)
return point
