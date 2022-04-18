# university-info-parser
Parses through my university posts and throws them into a JSON file.

Um tempo atrás descobri que no portal da minha universidade, a URL me permite navegar por diversos posts de outros cursos e outras matérias. Então, fiz um script para percorrer esses posts, coletar informações e mostrar links para acesso de diferentes matérias em um site feito em React.

O arquivo JSON gerado registra o ID do post, Título, Matéria, Professor, URL do post e URL da matéria. Ele então é filtrado no site React para mostrar somente a matéria e URL da matéria, afim de deixar o site mais performático, levando em consideração que milhares de posts fariam o site extremamente lento.

### Como iniciar
- Preencher o arquivo ```options.json``` na pasta raiz com um arquivo JSON com as chaves id (matrícula no portal), password (senha no portal), phone_number (número de telefone registrado na API do CallmeBot) e callmebot_api_key (API Key do Call me Bot). Este dois últimos são opcionais.  
- ```python main.py``` na pasta principal para iniciar o script.
- ```cd react-website/website``` para acessar a pasta do site em React.
- ```yarn``` para instalar as dependências do projeto.
- ```yarn start``` para iniciar o site em React no modo de desenvolvimento.

### Script
- Utiliza Selenium para criar um browser virtual e acessar o portal.
- CallMeBot API manda uma mensagem por Whatsapp caso o bot pare de funcionar.
- Registra tudo em um arquivo JSON, e em um arquivo que exporta um objeto JS para o site em React utilizar.
- O script loga no portal da UVV e começa a acessar os posts em ordem. Caso ele pare, registra onde parou e ao iniciar novamente ele resume.

### Site em React
- O site em React está bem simples e só lista as matérias e os links para as matérias, mas pode também listar os posts. Porém, necessitaria de uma paginação pois são muitos posts.
- Utilizei o Styled Components para estilizar a página.
- Ele percorre o JSON criado pelo script com todos os posts registrados, filtra por matéria e por link da matérias.

