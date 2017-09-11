https://github.com/scanse/sweep-ros

#步骤
- 要先安装sweep-sdk 
- mkdir github
- cd github/
- git clone https://github.com/scanse/sweep-sdk
- cd sweep-sdk/libsweep/
- mkdir -p build
- cd build/
- cmake .. -DCMAKE_BUILD_TYPE=Release
- cmake --build .
- sudo cmake --build . --target install
- sudo ldconfig
- cd ..
- git clone https://github.com/scanse/sweep-ros.git