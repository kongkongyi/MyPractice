

print('\n'.join([''.join(["%s*%s=%-3s" %(x, y, y*x) for x in range(1,y+1)]) for y in range(1,10)]))

[print('{}*{}={:<3}{}'.format(j, i, i*j, '\n' if i==j else ''),end="") for i in range(1,10) for j in range(1, i+1)]

['{:04}.{}'.format(i,''.join([random.choice(bytes(range(97,123)).decode()) for _ in range(10)])) for i in range(1,10)] 

['{:04}.{}'.format(i,''.join([random.choice(string.ascii_lowercase) for _ in range(10)])) for i in range(1,10)] 

['{:04}.{}'.format(i,''.join([chr(random.randint(97,122)) for _ in range(10)])) for i in range(1,10)]
