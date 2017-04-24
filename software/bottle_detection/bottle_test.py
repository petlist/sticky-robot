import bottle

det_0 = [10,10]
bottle1 = bottle.Bottle(det_0, [100,100], 'Bottle_1')
print(bottle1.get_num_det())

det_1 = [11,11]
bottle1.add_detection_manually(det_1)
print(bottle1.get_num_det())

bottle1.set_eps(0.05)
print(bottle1.eps)

det_test = [50,50]
print(type(bottle1.get_dist(det_test)))
print(bottle1.get_dist(det_test))

bottle1.part_of_bottle(det_test)

"""
imagesize = [100, 100]
print('imagesize ' + str(imagesize[0]))
det_2 = [15,10]
det_3 = [17,10]
bottle1.part_of_bottle(det_2)
bottle1.part_of_bottle(det_3)
bottle1.set_eps(0.1)
bottle1.part_of_bottle(det_3)
"""