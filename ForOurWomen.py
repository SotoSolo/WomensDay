import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


encoded_message = [89, 111, 117, 114, 32, 87, 105,
                   115, 100, 111, 109, 44, 32, 83,
                   116, 114, 101, 110, 103, 116, 104,
                   44, 32, 97, 110, 100, 32, 67, 111,
                   109, 112, 97, 115, 115, 105, 111, 110,
                   32, 73, 110, 115, 112, 105, 114, 101, 32,
                   85, 115, 32, 65, 108, 108]


def decode_message(encoded_list):
    return ''.join([chr(c) for c in encoded_list])


decoded_message = decode_message(encoded_message)

print("In honor of Women's Day, a special analysis reveals:")
print(decoded_message)

t = np.linspace(0, 2 * np.pi, 100)
x = 16 * np.sin(t)**3
y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)

plt.figure(figsize=(8, 7))
plt.plot(x, y, color='red')
plt.axis('off')
plt.show()
