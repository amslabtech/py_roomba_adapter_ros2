FROM ubuntu:18.04

SHELL ["/bin/bash", "-c"]

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -q -y \
        curl \
        gnupg2 \
        lsb-release \
        wget \
        libsm6 \
        libxext6 \
        libxrender-dev \
    && rm -rf /var/lib/apt/lists/*

RUN curl http://repo.ros2.org/repos.key | apt-key add -

RUN sh -c 'echo "deb [arch=amd64,arm64] http://packages.ros.org/ros2/ubuntu `lsb_release -cs` main" > /etc/apt/sources.list.d/ros2-latest.list'

RUN apt-get update && apt-get install --no-install-recommends -y \
        git \
        python3-pip \
        python3-rospkg \
        python3-catkin-pkg \
        python3-colcon-common-extensions \
        python3-rosdep \
        python3-vcstool \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install -U \
        pyroombaadapter

RUN apt-get update && apt-get install -y \
        ros-dashing-ros-base \
        ros-dashing-cv-bridge \
    && rm -rf /var/lib/apt/lists/*

RUN echo "source /opt/ros/dashing/setup.bash" >> /root/.bashrc

WORKDIR /root

RUN mkdir -p ros2_ws/src

WORKDIR /root

COPY ./ros_entrypoint.sh /
CMD ["/ros_entrypoint.sh"]
