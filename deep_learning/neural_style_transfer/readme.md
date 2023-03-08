This project is used from already existing paper: [research paper 2016](https://www.cv-foundation.org/openaccess/content_cvpr_2016/papers/Gatys_Image_Style_Transfer_CVPR_2016_paper.pdf)
and [reasearch paper 2018](https://arxiv.org/pdf/1602.07188.pdf)

and most of the code and content/stytle images from (github)[https://github.com/gordicaleksa/pytorch-neural-style-transfer]

Here rather than implementing this paper again from scratch I tried to use it as I got from the code and describe in paper to understand and manipulate to get better understanding of it.

This Model seems to be slow in case of Adam and in lbfgs little bit fast but needs good computation power. 

This is old model developed in 2016 and optimized with content image rather than noise in 2018. 


## Acknowledgements

I found these repos useful: (while developing this one)
* [fast_neural_style](https://github.com/pytorch/examples/tree/master/fast_neural_style) (PyTorch, feed-forward method)
* [neural-style-tf](https://github.com/cysmith/neural-style-tf/) (TensorFlow, optimization method)
* [neural-style](https://github.com/anishathalye/neural-style/) (TensorFlow, optimization method)

I found some of the content/style images I was using here:
* [style/artistic images](https://www.rawpixel.com/board/537381/vincent-van-gogh-free-original-public-domain-paintings?sort=curated&mode=shop&page=1)
* [awesome figures pic](https://www.pexels.com/photo/action-android-device-electronics-595804/)
* [awesome bridge pic](https://www.pexels.com/photo/gray-bridge-and-trees-814499/)

Other images are now already classics in the NST world.

