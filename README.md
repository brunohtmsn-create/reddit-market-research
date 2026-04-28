# 📊 Reddit Market Research Tool

Ferramenta educacional para análise de tendências e validação de ideias de produtos/serviços através de dados públicos do Reddit.

## 🎯 Objetivo

Identificar problemas recorrentes, tendências emergentes e oportunidades de mercado através da análise ética de discussões em comunidades do Reddit.

## ✨ Funcionalidades

- ✅ Análise de problemas/dores em comunidades específicas
- ✅ Identificação de tópicos em alta
- ✅ Métricas de engajamento (upvotes, comentários)
- ✅ Exportação de dados para análise posterior
- ✅ Respeito total aos rate limits da API

## 🔧 Instalação

```bash
# Clonar repositório
git clone https://github.com/seu-usuario/reddit-market-research.git
cd reddit-market-research

# Instalar dependências
pip install praw
```

## 🚀 Uso

### 1. Obter Credenciais Reddit

1. Acesse: https://www.reddit.com/prefs/apps
2. Clique em "create another app" ou "are you a developer? create an app..."
3. Preencha:
   - **Name:** Market Research Tool
   - **Type:** script
   - **Redirect URI:** http://localhost:8000
4. Copie o **Client ID** e **Client Secret**

### 2. Configurar

```python
from reddit_market_research import RedditMarketResearch

# Suas credenciais
CLIENT_ID = "abc123..."
CLIENT_SECRET = "xyz789..."
USER_AGENT = "MarketResearch/1.0 by /u/seu_username"

# Inicializar
researcher = RedditMarketResearch(CLIENT_ID, CLIENT_SECRET, USER_AGENT)
```

### 3. Analisar Tendências

```python
# Buscar problemas com automação
pain_points = researcher.analyze_pain_points(
    keyword='automation',
    subreddits=['Entrepreneur', 'smallbusiness', 'SaaS'],
    time_filter='month',
    limit=50
)

# Ver resultados
for post in pain_points[:10]:
    print(f"{post['title']} - {post['score']} upvotes")
```

## 📋 Casos de Uso

### 1. Validação de Produto

Identifique se existe demanda real para sua ideia de produto:

```python
results = researcher.analyze_pain_points(
    keyword='email automation',
    subreddits=['marketing', 'Entrepreneur', 'smallbusiness'],
    time_filter='month'
)

# Análise: Há problemas recorrentes? Quantas pessoas estão falando sobre isso?
```

### 2. Pesquisa de Competição

Veja como competidores são discutidos:

```python
results = researcher.analyze_pain_points(
    keyword='mailchimp alternatives',
    subreddits=['marketing', 'emailmarketing'],
    time_filter='year'
)
```

### 3. Identificação de Tendências

Descubra tópicos emergentes:

```python
trending = researcher.get_trending_topics('technology', limit=50)

# Filtre por crescimento recente e alto engajamento
```

## 🛡️ Uso Ético

Esta ferramenta foi desenvolvida com foco em **uso ético e responsável**:

- ✅ **Somente leitura** de dados públicos
- ✅ **Respeita rate limits** da API do Reddit
- ✅ **Não faz spam** ou postagens automatizadas
- ✅ **Não coleta dados pessoais** de usuários
- ✅ **Segue termos de uso** do Reddit

## ⚠️ Rate Limits

A Reddit API tem limites de requisições:

- **60 requests por minuto** para scripts
- **600 requests por 10 minutos**

O código respeita automaticamente esses limites através do PRAW.

## 📊 Exemplo de Output

```json
{
  "subreddit": "Entrepreneur",
  "title": "Struggling with email follow-ups - any automation tips?",
  "score": 247,
  "num_comments": 68,
  "upvote_ratio": 0.94,
  "url": "https://reddit.com/..."
}
```

## 🤝 Contribuindo

Contribuições são bem-vindas! Por favor:

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📜 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 🔗 Links Úteis

- [Reddit API Documentation](https://www.reddit.com/dev/api/)
- [PRAW Documentation](https://praw.readthedocs.io/)
- [Reddit API Terms](https://www.reddit.com/wiki/api-terms)

## ⚖️ Disclaimer

Esta ferramenta é destinada apenas para fins educacionais e de pesquisa de mercado ética. 

**Não use para:**
- ❌ Spam
- ❌ Scraping em massa
- ❌ Violação de privacidade
- ❌ Manipulação de comunidades

Use com responsabilidade e respeite a comunidade do Reddit.

---

**Desenvolvido por:** [Seu Nome]  
**Contato:** [Seu Email]  
**Licença:** MIT
