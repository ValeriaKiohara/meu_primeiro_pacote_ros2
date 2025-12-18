from setuptools import setup

package_name = 'meu_primeiro_pacote'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='seu_nome',
    maintainer_email='seu@email.com',
    description='Primeiro pacote ROS 2',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
    'console_scripts': [
        'primeiro_node = meu_primeiro_pacote.primeiro_node:main',
        'subscriber_node = meu_primeiro_pacote.subscriber_node:main',
        'cmd_vel_pub = meu_primeiro_pacote.cmd_vel_pub:main',
    ],
},

)
