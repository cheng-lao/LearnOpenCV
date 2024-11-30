#include<opencv2/opencv.hpp>
#include<iostream>
#include<string>
#include "opencv2/core/hal/interface.h"
#include <filesystem>
using namespace std;
using namespace cv;

int main(){
    //这里好像不能使用相对路径
    string imagePath = "/home/chengyingjie666/code/learnOpencv/images/230501201_1.jpg";
    cv::Mat img = cv::imread(imagePath, 1);

    // 打印文件路径
    cout << "Image path: " << imagePath << endl;

    // 检查文件是否存在
    if (!filesystem::exists(imagePath)) {
        cerr << "Error: File does not exist at path " << imagePath << endl;
        return -1;
    }

    if (img.empty()) {
        cerr << "Error: Could not open or find the image" << endl;
        return -1;
    }
    // swap channles and assign new order channels into a new mat,and imshow both mat.
    vector<cv::Mat> channels;
    cv::split(img, channels);
    cv::Mat new_image;
    cv::swap(channels[0], channels[1]);
    cv::merge(channels, new_image);

    cv::imshow("image-bgr", img);
    cv::imshow("new-image-rgb", new_image);
    cv::waitKey(0);
    return 0;
}

