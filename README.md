# mapper_and_reducer_SystemProgramming
"Mapper and Reducer" System Programming, Sogang University, 2019 Spring Season

## Overview
이 프로젝트는 Hadoop과 MapReduce의 기초에 대해 이해하는 것을 목적으로 하는 프로젝트입니다.

## Main Probelm
* Group by max
정수와 콤마, 그리고 실수로 이루어진 파일을 읽어들여 정수 부분의 그룹에서 가장 값이 큰 값을 그룹별로 출력하기 위한 문제이다.

<img src = "https://i.ibb.co/68xw7Zh/1.png"/>

input.data를 generate.py를 이용하여 16개의 그룹으로 나뉘어진 1억 개의 실수로 만들고, Hadoop MapReduce를 이용하여 결과를 출력한다.

## Module Definition
* mapper.py
파일을 읽어 들여와 ‘콤마’로 group (정수 부분)과 number (실수 부분)을 split()함수를 이용해 분리하여 mapping하고, 그것을 출력한다.

* reducer.py
mapper.py에서 출력된 것을 파일로 읽어들여 콤마로 구분하여 group과 number을 분리하고, number은 문자열이므로 실수화를 시켜 준다. data라는 딕셔너리의 key는 group이 되고, 해당 group에 number의 최대값을 max함수를 이용하여 넣어 준다. 마지막으로 ValueError을 except 시켜 pass 한다.
그리고 결과를 출력한다.

