# Meu primeiro pacote ROS2

## Descrição
Este repositório contém um **pacote acadêmico em ROS 2 (Python)** desenvolvido com o objetivo de **aprender e demonstrar os conceitos fundamentais do ROS 2**, incluindo comunicação entre nós, publicação e subscrição de tópicos e controle de movimento de um robô móvel em ambiente simulado.

O pacote foi testado utilizando **ROS 2 Humble** em **Ubuntu 22.04**, com simulação no **Gazebo** e visualização no **RViz2**, usando o modelo **TurtleBot3**.

---

## Objetivos Acadêmicos
- Compreender a arquitetura do ROS 2
- Criar e executar **nós (nodes)** em Python
- Implementar **publishers e subscribers**
- Trabalhar com mensagens do tipo `Twist`
- Publicar comandos de velocidade no tópico `/cmd_vel`
- Controlar um robô móvel em simulação
- Servir como base para projetos futuros em robótica móvel e navegação autônoma

---

## Estrutura do Pacote
meu_primeiro_pacote/
├── meu_primeiro_pacote/
│ ├── init.py
│ ├── primeiro_node.py # Publisher simples
│ ├── subscriber_node.py # Subscriber simples
│ └── cmd_vel_pub.py # Publicador de /cmd_vel
├── package.xml
├── setup.py
├── setup.cfg
└── resource


---

## Funcionalidades Implementadas

### 🔹 Publisher básico
Publica mensagens do tipo `String` em um tópico de teste.

### 🔹 Subscriber básico
Assina um tópico e imprime as mensagens recebidas no terminal.

### 🔹 Controle de movimento
Publica mensagens do tipo `geometry_msgs/Twist` no tópico `/cmd_vel`, permitindo:
- Movimento linear
- Rotação do robô
- Testes de controle em simulação

---

## Requisitos
- Ubuntu 22.04
- ROS 2 Humble
- Gazebo
- RViz2
- TurtleBot3 packages

Instalação dos pacotes necessários:
```bash
sudo apt update
sudo apt install ros-humble-turtlebot3* ros-humble-turtlebot3-simulations


Compilação do Pacote

Dentro do workspace ROS 2:

cd ~/ros2_ws
colcon build
source install/setup.bash

Como Executar
Executar o publisher simples
ros2 run meu_primeiro_pacote primeiro_node

Executar o subscriber
ros2 run meu_primeiro_pacote subscriber_node

Executar o publicador de velocidade (/cmd_vel)
ros2 run meu_primeiro_pacote cmd_vel_pub

Simulação no Gazebo (TurtleBot3)

Abrir o ambiente simulado:

export TURTLEBOT3_MODEL=burger
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py


Executar o nó de controle de movimento:

ros2 run meu_primeiro_pacote cmd_vel_pub

Aplicações Futuras

Este pacote pode ser estendido para:

Integração com sensores (LiDAR, IMU)

SLAM (mapeamento)

Navegação autônoma com Nav2

Migração para robô físico

Autora

Valeria Kiohara
Projeto acadêmico para estudo de Robótica e ROS 2

Licença

Este projeto é de uso acadêmico e educacional.
