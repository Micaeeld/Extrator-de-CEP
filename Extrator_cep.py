endereco = 'Rua iracema, 13, Jardim limoeiro, Serra, ES, 29164002'
import re  # Regular Expression -- RegEx



padrao = re.compile('[0-9]{5}[-]?[0-9]{3}') #[0-9] numeros de 0 até 9 {5} 5 desses numeros de 0-9 [-]? interrogação = pode ou nao ter '-'
busca = padrao.search(endereco)  # Match
if busca:
    cep = busca.group()
    print(cep)