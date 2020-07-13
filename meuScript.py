import vrep
import time
import random
import math

clientID = vrep.simxStart('127.0.0.1', 19999, True, True, 5000, 5)

if (clientID == 0):
    print('Conectadah!')

returnC, LwMotor = vrep.simxGetObjectHandle(clientID, 'Motor_Esquerdo', vrep.simx_opmode_oneshot_wait)
returnC, RwMotor = vrep.simxGetObjectHandle(clientID, 'Motor_Direito', vrep.simx_opmode_oneshot_wait)
vrep.simxSetJointTargetVelocity(clientID, LwMotor, 1, vrep.simx_opmode_streaming)
vrep.simxSetJointTargetVelocity(clientID, RwMotor, 1, vrep.simx_opmode_streaming)
returnC, carHandle = vrep.simxGetObjectHandle(clientID, 'Carro', vrep.simx_opmode_oneshot_wait)
print ('car handle: ' + str(carHandle))

for i in range (0,2):
    vrep.simxStartSimulation(clientID, vrep.simx_opmode_oneshot_wait)
    print('Simulação iniciadah')

    xy, carroPosicao = vrep.simxGetObjectPosition(clientID, carHandle, -1, vrep.simx_opmode_streaming)
    print ('Posicao do carro: x = ' + str(carroPosicao[0]) + ', y = ' + str(carroPosicao[1]))
    for j in range(0,3):
        x = random.randint(0, 350)
        y = random.randint(0, 350)
        print ('Posicoes: ' + str(x) + '  ' + str(y))
        vrep.simxSetJointTargetPosition(clientID, LwMotor, math.radians(x), vrep.simx_opmode_oneshot_wait)
        vrep.simxSetJointTargetPosition(clientID, RwMotor, math.radians(y), vrep.simx_opmode_oneshot_wait)
        time.sleep(2)

        esquerdo = vrep.simxGetJointPosition(clientID, LwMotor, vrep.simx_opmode_oneshot_wait)
        direito = vrep.simxGetJointPosition(clientID, RwMotor, vrep.simx_opmode_oneshot_wait)
        print ('Atingiram as posições: ' + str(x) + '   ' + str(y))

        #posicao do carro apos a sequencia de movimentos:
        posSeq, carroPosicao = vrep.simxGetObjectPosition(clientID, carHandle, -1, vrep.simx_opmode_buffer)
        print('posição do carro: x = ' + str(carroPosicao[0]) + ', y = ' + str(carroPosicao[1]))

        #orientacao do carro apos a sequencia de movimentos
        posSq, carroOrientacao = vrep.simxGetObjectOrientation(clientID, carHandle, -1, vrep.simx_opmode_buffer)
        print('orientação do carro: x = ' + str(carroOrientacao[1]) + ', y = ' + str(carroOrientacao[2]))

vrep.simxStopSimulation(clientID, vrep.simx_opmode_oneshot_wait)
time.sleep(1)

print ('Fim da simulação')

vrep.simxFinish(clientID)
time.sleep(1)
