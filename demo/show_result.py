import matplotlib.pyplot as plt

images_name = ['walkers', 'walkers2', 'walkers3', 'walkers4']
models_name = ['val image', 'Faster R-CNN', 'Mask R-CNN']

plot_index = 0

row = len(images_name)
col = len(models_name)
figure = plt.figure(num='compare')

for i in range(row):
    for j in range(col):
        if j == 0:
            subplot = plt.imread('/home/kuangbixia/projects/mmdetection/data/' + images_name[i] + '.jpeg')
        elif j==1:
            subplot = plt.imread('/home/kuangbixia/projects/mmdetection/demo/results/faster_rcnn/coco_' + images_name[i] + '.png')
        else:
            subplot = plt.imread('/home/kuangbixia/projects/mmdetection/demo/results/mask_rcnn/' + images_name[i] + '.png')
        plot_index += 1
        plt.subplot(row, col, plot_index)
        plt.imshow(subplot)
        plt.axis('off')
        if i == 0:
            plt.title(models_name[j])
plt.show()