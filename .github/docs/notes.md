# Anotações Módulo 3 - Desenvolvimento de APIs com Flask

> [voltar](../../README.md) para a página anterior

## Sumário

- [Anotações Módulo 3 - Desenvolvimento de APIs com Flask](#anotações-módulo-3---desenvolvimento-de-apis-com-flask)
  - [Sumário](#sumário)
  - [Conteúdo](#conteúdo)
    - [O que é API?](#o-que-é-api)
    - [O que são Métodos de Requisição HTTP?](#o-que-são-métodos-de-requisição-http)
  - [Códigos de Status de Respostas HTTP](#códigos-de-status-de-respostas-http)
    - [O que é Flask?](#o-que-é-flask)

## Conteúdo

### O que é API?

Uma API, ou Interface de Programação de Aplicações, é um conjunto de regras e definições que permite que softwares diferentes se comuniquem entre si. Ela define as maneiras pelas quais diferentes componentes de software devem interagir, oferecendo um conjunto de métodos, funções e protocolos que facilitam a integração e a comunicação entre sistemas.

As APIs desempenham um papel crucial na conectividade e interoperabilidade de sistemas, permitindo que desenvolvedores utilizem funcionalidades específicas de uma aplicação ou serviço sem precisar entender sua implementação interna. Isso promove a reutilização de código, acelera o desenvolvimento de software e facilita a integração entre diferentes plataformas.

**Documentação Oficial:** [Mozilla Developer Network (MDN) - API](https://developer.mozilla.org/pt-BR/docs/Glossary/API)

> [retornar](#anotações-módulo-3---desenvolvimento-de-apis-com-flask) para o topo da página

### O que são Métodos de Requisição HTTP?

Os métodos de requisição HTTP são verbos ou ações que indicam a natureza da solicitação feita ao servidor. Cada método representa uma operação diferente e tem um significado específico. Aqui estão alguns dos métodos de requisição HTTP mais comuns:

1. **GET**: Solicita dados de um recurso especificado. Os parâmetros de consulta podem ser anexados à URL.

2. **POST**: Submete dados para serem processados para um recurso especificado. É muitas vezes utilizado para enviar dados de formulário para o servidor.

3. **PUT**: Atualiza um recurso especificado com os dados fornecidos. Se o recurso não existir, ele pode criar um novo recurso com o URI fornecido.

4. **DELETE**: Remove o recurso especificado.

5. **PATCH**: Aplica modificações parciais a um recurso.

6. **OPTIONS**: Retorna os métodos HTTP que o servidor suporta para um determinado URL. Isso pode ser usado para verificar as opções disponíveis antes de enviar uma solicitação.

7. **HEAD**: Retorna apenas os cabeçalhos (headers) da resposta, sem o corpo do recurso. Pode ser usado para obter metadados sem recuperar o corpo da resposta.

8. **TRACE**: Realiza um teste de loop-back ao longo do caminho de comunicação até o recurso de destino. Isso pode ser usado para depuração.

9. **CONNECT**: Usado para estabelecer uma conexão de túnel ao servidor identificado pelo recurso.

Aqui está a documentação oficial da Mozilla Developer Network (MDN) sobre métodos de requisição HTTP:
[MDN Web Docs - Métodos de Requisição HTTP](https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Methods)

Essa documentação fornece informações detalhadas sobre cada método, suas finalidades e como eles devem ser utilizados.

> [retornar](#anotações-módulo-3---desenvolvimento-de-apis-com-flask) para o topo da página

## Códigos de Status de Respostas HTTP

Códigos de status de respostas HTTP são códigos numéricos que indicam o resultado da tentativa do cliente de solicitar dados de um servidor. Cada código de status é uma mensagem de três dígitos, onde o primeiro dígito define a classe do código de status e os dois dígitos seguintes não têm qualquer papel de categorização. Existem cinco classes de códigos de status HTTP:

1. **1xx (Informational):** A requisição foi recebida, continuará processando.

2. **2xx (Successful):** A requisição foi recebida, compreendida e aceita com sucesso.

3. **3xx (Redirection):** A requisição precisa de ações adicionais para ser completada.

4. **4xx (Client Error):** O cliente parece ter feito algo errado.

5. **5xx (Server Error):** O servidor falhou em atender a uma requisição aparentemente válida.

Aqui estão alguns exemplos de códigos de status comuns:

- **200 OK:** A requisição foi bem-sucedida.

- **201 Created:** A requisição foi bem-sucedida e um novo recurso foi criado como resultado.

- **204 No Content:** A requisição foi bem-sucedida, mas não há informações a serem enviadas no corpo da resposta.

- **400 Bad Request:** A requisição não pôde ser compreendida ou foi malformada.

- **401 Unauthorized:** A requisição requer autenticação do usuário.

- **403 Forbidden:** O servidor entende a requisição, mas se recusa a atendê-la.

- **404 Not Found:** O recurso requisitado não foi encontrado no servidor.

- **500 Internal Server Error:** Um erro genérico de servidor ocorreu.

Para obter informações mais detalhadas sobre os códigos de status HTTP, você pode consultar a documentação oficial do Mozilla Developer Network (MDN). Aqui está o link para a seção relevante: [Documentação MDN sobre Códigos de Status HTTP](https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Status)

> [retornar](#anotações-módulo-3---desenvolvimento-de-apis-com-flask)

### O que é Flask?

Flask é um framework web leve e poderoso para Python, utilizado para desenvolver aplicações web. Ele é conhecido por sua simplicidade e facilidade de uso, permitindo aos desenvolvedores criar aplicações web rapidamente. Flask é extensível e segue o princípio do "faça o mínimo necessário" (micro-framework), o que significa que ele fornece apenas as ferramentas básicas necessárias para construir uma aplicação web, deixando espaço para que os desenvolvedores escolham e integrem as bibliotecas e ferramentas adicionais que preferirem.

Principais características do Flask:

1. **Micro-framework:** Oferece o mínimo necessário para começar, permitindo que os desenvolvedores escolham as ferramentas que desejam adicionar.

2. **Fácil de aprender e usar:** A sintaxe simples e a estrutura intuitiva tornam o Flask acessível a desenvolvedores iniciantes.

3. **Extensibilidade:** Flask suporta extensões que adicionam funcionalidades específicas, permitindo aos desenvolvedores personalizar suas aplicações de acordo com suas necessidades.

4. **Flask-WTF:** Uma extensão que integra o WTForms com o Flask, facilitando a validação de formulários.

5. **Jinja2:** Flask usa o mecanismo de template Jinja2 para criar páginas HTML dinâmicas.

6. **Desenvolvimento rápido:** Permite criar protótipos e desenvolver aplicações web de forma rápida.

7. **Integração com outras tecnologias:** Pode ser facilmente integrado com outros componentes e bibliotecas, como SQLAlchemy para manipulação de banco de dados.

Para mais informações detalhadas, consulte a [documentação oficial do Flask](https://flask.palletsprojects.com/).

> [retornar](#anotações-módulo-3---desenvolvimento-de-apis-com-flask) para o topo da página
>
> [voltar](../../README.md) para a página anterior
