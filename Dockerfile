FROM amazonlinux

WORKDIR /tflite

# Install development tools, Python 3.11, and CMake
RUN yum groupinstall -y development
RUN yum install -y python3.11 python3.11-devel
RUN yum install -y python3-pip

# Install necessary dependencies including Pybind11
RUN pip3 install numpy wheel setuptools pybind11

RUN yum install -y glib2-devel

RUN yum install -y cmake

# Clone TensorFlow repository
RUN git clone --branch v2.14.0-rc0 https://github.com/tensorflow/tensorflow.git

RUN cd ./tensorflow/tensorflow/lite/tools/pip_package/

# Build TensorFlow Lite package using CMake
RUN sh -x /tflite/tensorflow/tensorflow/lite/tools/pip_package/build_pip_package_with_cmake.sh

# Install the compiled TensorFlow Lite package
RUN pip3 install tensorflow/tensorflow/lite/tools/pip_package/gen/tflite_pip/python3/dist/tflite_runtime-2.14.0rc0-cp311-cp311m-linux_x86_64.whl

CMD tail -f /dev/null
