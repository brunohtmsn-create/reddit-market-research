"""
Reddit Market Research Tool
===========================

Ferramenta educacional para análise de tendências e validação de ideias
através de dados públicos do Reddit.

Uso ético: Respeita rate limits, não faz spam, apenas leitura de dados públicos.

Autor: Bruno Conde
Licença: MIT
"""

import praw
from datetime import datetime
import json

class RedditMarketResearch:
    """
    Classe para análise ética de tendências no Reddit
    """
    
    def __init__(self, client_id, client_secret, user_agent):
        """
        Inicializa conexão com Reddit API
        
        Args:
            client_id: Reddit app client ID
            client_secret: Reddit app secret
            user_agent: User agent string (formato: appname/version by /u/username)
        """
        self.reddit = praw.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            user_agent=user_agent
        )
        
        # Verificar conexão
        print(f"✅ Conectado ao Reddit como: {self.reddit.read_only}")
    
    def analyze_pain_points(self, keyword, subreddits, time_filter='month', limit=50):
        """
        Analisa problemas/dores recorrentes em comunidades
        
        Args:
            keyword: Palavra-chave para buscar
            subreddits: Lista de subreddits para analisar
            time_filter: Filtro de tempo ('day', 'week', 'month', 'year')
            limit: Número máximo de posts por subreddit
            
        Returns:
            Lista de posts relevantes com métricas
        """
        results = []
        
        for subreddit_name in subreddits:
            try:
                subreddit = self.reddit.subreddit(subreddit_name)
                
                # Buscar posts relacionados ao keyword
                for submission in subreddit.search(keyword, 
                                                   time_filter=time_filter, 
                                                   limit=limit):
                    
                    # Filtrar apenas posts com engajamento significativo
                    if submission.score > 10:
                        results.append({
                            'subreddit': subreddit_name,
                            'title': submission.title,
                            'score': submission.score,
                            'num_comments': submission.num_comments,
                            'created_utc': submission.created_utc,
                            'url': submission.url,
                            'upvote_ratio': submission.upvote_ratio
                        })
                        
            except Exception as e:
                print(f"⚠️ Erro em r/{subreddit_name}: {e}")
                continue
        
        # Ordenar por engajamento
        results.sort(key=lambda x: x['score'], reverse=True)
        
        return results
    
    def get_trending_topics(self, subreddit_name, limit=25):
        """
        Identifica tópicos em alta em um subreddit
        
        Args:
            subreddit_name: Nome do subreddit
            limit: Número de posts para analisar
            
        Returns:
            Lista de posts em alta
        """
        subreddit = self.reddit.subreddit(subreddit_name)
        
        trending = []
        
        for submission in subreddit.hot(limit=limit):
            trending.append({
                'title': submission.title,
                'score': submission.score,
                'num_comments': submission.num_comments,
                'created_utc': submission.created_utc,
                'url': submission.url
            })
        
        return trending
    
    def export_results(self, data, filename='research_results.json'):
        """
        Exporta resultados para arquivo JSON
        
        Args:
            data: Dados para exportar
            filename: Nome do arquivo de saída
        """
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        print(f"✅ Resultados salvos em: {filename}")


# Exemplo de uso
if __name__ == "__main__":
    # Configuração (substituir com suas credenciais)
    CLIENT_ID = "seu_client_id_aqui"
    CLIENT_SECRET = "seu_client_secret_aqui"
    USER_AGENT = "MarketResearch/1.0 by /u/seu_username"
    
    # Inicializar
    researcher = RedditMarketResearch(CLIENT_ID, CLIENT_SECRET, USER_AGENT)
    
    # Exemplo 1: Analisar problemas com automação
    print("\n🔍 Analisando problemas com automação...")
    pain_points = researcher.analyze_pain_points(
        keyword='automation',
        subreddits=['Entrepreneur', 'smallbusiness', 'SaaS'],
        time_filter='month',
        limit=30
    )
    
    print(f"\n📊 Encontrados {len(pain_points)} posts relevantes")
    
    # Mostrar top 5
    for i, post in enumerate(pain_points[:5], 1):
        print(f"\n{i}. {post['title']}")
        print(f"   ↑ {post['score']} | 💬 {post['num_comments']} comentários")
        print(f"   🔗 {post['url']}")
    
    # Exemplo 2: Tópicos em alta
    print("\n\n🔥 Tópicos em alta em r/Entrepreneur...")
    trending = researcher.get_trending_topics('Entrepreneur', limit=10)
    
    for i, topic in enumerate(trending[:5], 1):
        print(f"{i}. {topic['title']} (↑ {topic['score']})")
    
    # Exportar resultados
    researcher.export_results(pain_points, 'automation_pain_points.json')
    
    print("\n✅ Análise concluída!")
    print("\n⚠️ Lembre-se de usar de forma ética e respeitar rate limits!")
