PAPERS = {
    "truthfulqa-2022": {
            "title": "TruthfulQA: Measuring How Models Mimic Human falsehoods",

            "authors":[
                "Stephanie Lin",
                "Jacob Hilton",
                "Owain Evans"
            ],

            "year": 2022,
            "venue": "ACL 2022",
            "source": {
                "doi": "10.18653/v1/2022.acl-long.229",
                "url": "https://aclanthology.org/2022.acl-long.229/",
                "arxiv": "https://arxiv.org/abs/2109.07958"
        },

        #What researchers actually investigated

        "research": {
            "question": (
                "Can language models avoid producing false answers"
                "when questions activate common human misconceptions?"
            ),

            "problem": (
                "Models learn from human-generated text."
                "That text contains both facts and mimsconceptions."
            ),

            "experiment" : {
                "benchmark": "TruthfulQA",
                "questions": 817,
                "categories": 38,

                "model_tested": [
                    "GPT-3",
                    "GPT-Neo/J",
                    "GPT-2",
                    "UnifiedQA (T5-based)"
                ]
            },

            "findings": [
                {
                    "id": "model_truthfulness",
                    "result": "58%",
                    "meaning": (
                        "The best-performing tested model "
                        "was truthful on 58% of questions."
                    ),
                    "source_location": "Abstract"
                },
                {
                    "id": "human_comparison",
                    "result": "94%",
                    "meaning": (
                        "Reported human performance on the benchmark."
                    ),
                    "source_location": "Abstract"
                },
                {
                    "id": "scaling",
                    "result": "Inverse scaling observed",
                    "meaning": (
                        "Larger models were generally less truthful "
                        "in the tested evaluations."
                    ),
                    "source_location": "Abstract"
                }
            ],

            "limitations": [
                "The benchmark was designed to test specific weakness.",
                "False answers do not demonstrate intentional deception.",
                "Results concern the models tested in this study.",
                "The benchmark does not measure every dimension "
                "of real-world AI reliability."
            ]
        }
    }
}

#Paperflix episodes

EPISODES = {
    "truthfulqa-ep01":{

    "id": "truthfulqa-ep01",
    "paper_id": "truthfulqa-2022",

    "series_id": "ai-that-lies",
    "episode_number": 1,

    "presentation" : {
        "title": "The AI That Couldn't Tell the Truth",

        "tagline": (
            "What happens when a machine learns from "
            "everything human write, including misconceptions?"
        ),

        "genre" : "AI Thriller",
        "difficulty": "Beginner",
        "estimated_minutes": 4,

        "thumbnail": {
            "headline": "CAN YOU TRUST ITS ANSWERS?",
            "visual": "An AI surrounded by conflicting information"
        }
    },
    "story": {

        "cold_open": (
            "Imagine asking an AI a simple question. "
            "It anwers immediately. Sounds confident. "
            "Even sounds convincing. But what if it is wrong? "
        ),

        "chapters" : [

            {
                "title": "The Problem",
                "narration": (
                    "AI models learn patterns from human-written "
                    "text. But humans have misconceptions, too. "
                    "Could a machine repeat these misconceptions "
                    "without recognising that they are false? "
                ),
                "evidence" : ["research_problem"]
            },

            {
                "title": "The Experiment",
                "narration" : (
                    "Three researchers created TruthfulQA, "
                    "a collection of 817 questions across "
                    "38 categories. These questions were "
                    "designed to expose common misconceptions. "
                    "They tested several language-model families. "
                ),
                "evidence": ["benchmark","models_tested"]
            },

            {
                "title": "The Unexpected Result",
                "narration": (
                    "The best-performing tested model was "
                    "truthful on only 58% of questions. "
                    "The reported human comparison was 94%. "
                    "The researchers also observed that larger "
                    "models were generally less truthful."

                ),
                "evidence": [
                    "model_truthfulness",
                    "human_comparison",
                    "scaling"
                ]
            },

            { 
                "title": "Why It Mattters",
                "narration": (
                    "Making a model larger does not automatically "
                    "make it more truthful. The researchers argued "
                    "that improving truthfulness may require "
                    "different training approaches."
                ),
                "evidence": ["scaling"]
            }
        ],

        "cliffhanger": ( 
            "If simply making AI biggerr isn't enough, "
            "can we train it to behave differently?"

            )
        },

        "science_card": {
            "key_takeaway": (
                "Language models can reproduce common misconceptions "
                "from human-generated text."
            ),

            "what_it_does_not_prove": [
                "That AI intentionally lies.",
                "That every AI model behaves this way.",
                "That all larger models are less truthful."
            ]
        },
        
        "navigation": {
            "next_episode_id": None,
            "previous_episode_id": None
        },
    "publication_status": "draft"

    }
}

SERIES = {
    "ai-that-lies": {
        "id": "ai-that-lies",
        "title": "AI That Lies?",

        "description": (
            "An exploration of AI truthfulness, "
            "deceptive behaviour and the challenges "
            "of trusting intellgent machines."
        ),
        "genre": "Psychological Thriller",
        "topic": "AI Safety",

        "cover": {
            "headline": "WHAT IF AI ISN'T TELLING THE TRUTH?",
            "visual" : "Cinematic mysterious AI laboratory"
        },

        "episode_ids":[
            "truthfulqa-ep01"
        ],

        "status": "in_development"
    }
}

