from agents.search_agent import run_search_agent
from agents.extraction_agent import run_extraction_agent
from agents.gap_agent import run_gap_agent
from agents.review_agent import run_review_agent, save_review
import time

def run_pipeline(topic: str):
    """
    Main pipeline — connects all 4 agents together
    """
    print("\n" + "🚀"*25)
    print("   AUTORESEARCH AGENT — PIPELINE STARTED")
    print("🚀"*25)
    print(f"\n📚 Research Topic: {topic}\n")
    
    start_time = time.time()

    # ── AGENT 1 — SEARCH ──
    papers = run_search_agent(topic, max_results=6)
    
    if not papers:
        print("❌ No papers found!! Please try a different topic.")
        return
    
    # ── AGENT 2 — EXTRACTION ──
    extracted_papers = run_extraction_agent(papers)
    
    if not extracted_papers:
        print("❌ Extraction failed!!")
        return
    
    # ── AGENT 3 — GAP ANALYSIS ──
    gap_analysis = run_gap_agent(extracted_papers, topic)
    
    if not gap_analysis:
        print("❌ Gap analysis failed!!")
        return
    
    # ── AGENT 4 — REVIEW GENERATOR ──
    review = run_review_agent(extracted_papers, gap_analysis, topic)
    
    if not review:
        print("❌ Review generation failed!!")
        return
    
    # ── SAVE REVIEW ──
    filename = save_review(review, topic)
    
    end_time = time.time()
    total_time = round(end_time - start_time, 2)

    print("\n" + "🎉"*25)
    print("   PIPELINE COMPLETED SUCCESSFULLY!!")
    print("🎉"*25)
    print(f"\n📊 Summary:")
    print(f"   📄 Papers found:     {len(papers)}")
    print(f"   🧠 Papers analyzed:  {len(extracted_papers)}")
    print(f"   💾 Review saved to:  {filename}")
    print(f"   ⏱️  Total time:       {total_time} seconds")
    print(f"\n✅ Your literature review is ready!!")
    print("🎉"*25 + "\n")
    
    return {
        "papers": papers,
        "extracted": extracted_papers,
        "gap_analysis": gap_analysis,
        "review": review,
        "filename": filename
    }


if __name__ == "__main__":
    print("\n" + "="*50)
    print("   🤖 AUTORESEARCH AGENT")
    print("   Built by: Shaik Arfa Anjum")
    print("   Powered by: Claude API + ArXiv + Semantic Scholar")
    print("="*50)
    
    # Get topic from user
    topic = input("\n🔍 Enter your research topic: ")
    
    if topic.strip():
        result = run_pipeline(topic)
    else:
        print("❌ Please enter a valid topic!!")