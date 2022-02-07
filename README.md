# ONG-de-Animais
Implementação de um sistema Orientado a Objetos em Python para gerenciamento de uma ONG de adoção de animais.

O sistema deve permitir o cadastro dos animais ao serem resgatados e o registro do processo de adoção. Deve conter o ano aproximado de nascimento, nome, sexo, se possui alguma doença, se está vacinado, se está castrado e a data de chegada na organização. Ao ser adotado, o sistema deve registrar a data de saída dos animais e também o adotante. 
Também serão cadastrados os voluntários da ONG, os doadores, os que disponibilizam um Lar Temporário para os animais e os adotantes. Deve incluir o nome, data de nascimento, telefone, gênero, e-mail e endereço. 

Cada animal fica abrigado em um lar temporário, oferecido por um voluntário. A capacidade máxima de qualquer lar temporário é de 1 animal. Nem todos os voluntários oferecem lar temporário, porém todos os lares temporários são disponibilizados por voluntários. A ONG possui um gasto mensal de R$100 reais por animal. Só é possível a entrada de um novo animal se a razão entre o valor total das doações no mês e quantidade de animais for maior em 100% do que o gasto mensal de um animal e se houver vaga para o animal em um lar temporário.

Deve ser possível listar os animais disponíveis para adoção, em ordem decrescente de tempo que foi resgatado pela ONG, os animais que foram adotados junto com seus respectivos adotantes e também o valor total das doações mensais.

Considerando os requisitos:
A ONG só aceita registro de Cães.
O registro de adoção só será possível se o adotante tiver 21 anos ou mais.
Para ser inserido na ONG, o animal precisa estar cadastrado e vacinado. 
A frequência de doação pelos doadores é mensal.
