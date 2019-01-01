'''

向pdf文档中写入多个图表

'''

import numpy

from matplotlib import pyplot as plot
from matplotlib.backends.backend_pdf import PdfPages

# Generate 15组正态分布随机数
data = numpy.random.randn(15, 1024)

# The PDF document
pdf_pages = PdfPages('histograms.pdf')

# Generate the pages

nb_plots = data.shape[0]  # 得到有多少组随机数（15组—）
nb_plots_per_page = 5  # 每页5组

nb_pages = int(numpy.ceil(nb_plots / float(nb_plots_per_page)))  # 计算页数
grid_size = (nb_plots_per_page, 1)  # 网格尺寸，5行1列

# 循环绘制15个图标
for i, samples in enumerate(data):
    # Create a figure instance (ie. a new page) if needed
    if i % nb_plots_per_page == 0:
        fig = plot.figure(figsize=(8.27, 11.69), dpi=100)

    # Plot stuffs !  grid_size：网格的尺寸
    plot.subplot2grid(grid_size, (i % nb_plots_per_page, 0))
    plot.hist(samples, 15, facecolor='#808080', alpha=0.75)

    # Close the page if needed
    if (i + 1) % nb_plots_per_page == 0 or (i + 1) == nb_plots:
        plot.tight_layout()
        pdf_pages.savefig(fig)

# Write the PDF document to the disk
pdf_pages.close()
