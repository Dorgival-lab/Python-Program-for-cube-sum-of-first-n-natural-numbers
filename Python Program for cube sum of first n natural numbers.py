# Programa Python eficiente para encontrar soma de cubos  
# dos primeiros n números naturais que evitam 
# transbordar se o resultado vai sair  
# limites.
  
# Retorna a soma das séries  
def sumOfSeries(n): 
    x = 0
    if n % 2 == 0 :  
        x = (n/2) * (n+1) 
    else: 
        x = ((n + 1) / 2) * n 
          
    return (int)(x * x) 
  
   
# Função Driver 
n = 5
print(sumOfSeries(n)) 
  
# Código Contribuído por Dorgival Fernando