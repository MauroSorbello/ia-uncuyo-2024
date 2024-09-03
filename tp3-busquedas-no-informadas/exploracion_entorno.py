import gymnasium as gym
import numpy as np
env = gym.make('FrozenLake-v1', render_mode='human')

# 2. Obtener informaci´on del entorno:
print("N´umero de estados:", env.observation_space.n)
print("N´umero de acciones:", env.action_space.n)

# 3. Ejecutar un episodio b´asico:
state = env.reset()
print("Posici´on inicial del agente:", state[0])
done = truncated = False
while not (done or truncated):
    action = env.action_space.sample() # Acci´on aleatoria
    next_state, reward, done, truncated, _ = env.step(action)
    print(f"Acci´on: {action}, Nuevo estado: {next_state}, Recompensa: {reward}")
    print(f"¿Gan´o? (encontr´o el objetivo): {done}")
    print(f"¿Fren´o? (alcanz´o el m´aximo de pasos posible): {truncated}\n")
    state = next_state

# 4)
# a) La funci´on make tiene como argumento is_slippery. ¿Qu´e controla dicho argumento?
# ¿Cu´al es su valor por defecto?
# El argumento is_slippery en FrozenLake, controla si las superficies del lago están resbaladizas o no.
# Cuando is_slippery es True, el agente puede deslizarse en una dirección diferente a la intencionada, haciendo que el entorno sea más impredecible y aumentando la dificultad. Esto simula un escenario en el que el terreno es resbaladizo, como el hielo.
# El valor por defecto de is_slippery es True. Esto significa que, a menos que se especifique lo contrario, el entorno tendrá superficies resbaladizas, añadiendo un elemento de aleatoriedad al movimiento del agente.

desc=[["S","F","F","F"], ["F","H","F","H"], ["F","F","F","H"], ["H","F","F","G"]]
gym.make('FrozenLake-v1', desc=desc, render_mode='human')
env_size = int(env.observation_space.n ** 0.5)
env_desc = env.unwrapped.desc
desc_str = [[cell.decode('utf-8') for cell in row] for row in env_desc]
print(desc_str)
print(f"Tamaño del entorno: {env_size}x{env_size}")
# Obtener el mapa del entorno y contar los agujeros usando env.unwrapped.desc
desc = env.unwrapped.desc  # Esto es un numpy.ndarray
holes = np.sum(desc == b'H')
print(f"Cantidad de agujeros: {holes}")
# Posicion inicial del agente siempre es (0,0)
# Posición del objetivo
goal_position = (env_size - 1, env_size - 1)
print(f"Posición del objetivo: {goal_position}")
