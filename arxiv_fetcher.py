import arxiv
import time

def fetch_arxiv_papers(topic: str, max_results: int = 8) -> list:
    """
    Fetch research papers from ArXiv based on a topic
    """
    print(f"🔍 Searching ArXiv for: {topic}")
    
    try:
        # Create search query
        search = arxiv.Search(
            query=topic,
            max_results=max_results,
            sort_by=arxiv.SortCriterion.Relevance
        )
        
        papers = []
        client = arxiv.Client()
        
        for result in client.results(search):
            paper = {
                "title": result.title,
                "authors": [author.name for author in result.authors[:3]],
                "abstract": result.summary[:500],
                "published": str(result.published.year),
                "url": result.entry_id,
                "source": "arxiv"
            }
            papers.append(paper)
            time.sleep(0.1)
        
        print(f"✅ Found {len(papers)} papers from ArXiv")
        return papers
    
    except Exception as e:
        print(f"❌ ArXiv Error: {e}")
        return []