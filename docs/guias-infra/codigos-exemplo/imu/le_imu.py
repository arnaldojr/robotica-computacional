#! /usr/bin/env python3
# -*- coding:utf-8 -*-

import rospy
import numpy as np
from geometry_msgs.msg import Twist, Vector3
from sensor_msgs.msg import Imu
from tf import transformations
import math


# funçao que le os dados da IMU 
def leu_imu(dado):
	quat = dado.orientation
    #cria a lista de quaternions com os eixos separados
	lista = [quat.x, quat.y, quat.z, quat.w]
    #faz a transformaçao de quaternion para angulos de euler
	angulos = np.degrees(transformations.euler_from_quaternion(lista))
    #cria o template da mensagem
	mensagem = """
    Tempo: {:}
    Orientação: {:.2f}, {:.2f}, {:.2f}
    Vel. angular: x {:.2f}, y {:.2f}, z {:.2f}\
    Aceleração linear:
    x: {:.2f}
    y: {:.2f}
    z: {:.2f}
    """.format(dado.header.stamp, angulos[0], angulos[1], angulos[2], dado.angular_velocity.x, dado.angular_velocity.y, dado.angular_velocity.z, dado.linear_acceleration.x, dado.linear_acceleration.y, dado.linear_acceleration.z)
    #exibe na mensagem os dados de angulo, velocidade angular e aceleracao linear ja convertidos para Roll, Pitch, e Yaw 
	print(mensagem)

	


if __name__=="__main__":

        #inicializa o node de conexao com o ROS
	rospy.init_node("le_imu")

        #Chama a função recebe_scan sempre que chegar um dado via ROS
	recebe_scan = rospy.Subscriber("/imu", Imu, leu_imu)

        #Loop do ROS
	while not rospy.is_shutdown():
        #sleep pra nao floodar o terminal
		rospy.sleep(1)
