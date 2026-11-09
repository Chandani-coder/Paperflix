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
                "Imagine asking an AI a question you genuinely "
                "don't know the answer to.\n\n"

                "It responds instantly. The answer sounds confident, "
                "well-written and convincing. You have no reason "
                "to doubt it.\n\n"

                "But what if the answer is actually a misconception "
                "that millions of people have repeated over the years?\n\n"

                "Three researchers decided to investigate exactly "
                "this kind of problem. And what they discovered "
                "challenged an assumption about increasingly "
                "powerful language models."
            ),

            # ======================================
            # STORY CHAPTERS
            # ======================================

            "chapters": [

                {
                    "title": "The Problem: When Being Convincing Isn't Being Correct",

                    "narration": (
                        "Language models learn by studying enormous "
                        "amounts of human-written text. They learn "
                        "patterns in language and become remarkably "
                        "good at predicting what words should come next.\n\n"

                        "But here's the problem. The internet contains "
                        "both accurate information and misconceptions. "
                        "Some false beliefs are repeated so frequently "
                        "that they become familiar to millions of people.\n\n"

                        "A model trained to imitate patterns in human "
                        "text can therefore learn to reproduce those "
                        "misconceptions when someone asks a question.\n\n"

                        "The researchers called these failures "
                        "\"imitative falsehoods\". The important idea "
                        "is that a false answer can be likely under "
                        "a model's training distribution, even though "
                        "it does not describe reality.\n\n"

                        "This is different from simply making a "
                        "calculation mistake. The problem is that "
                        "the training objective of predicting human "
                        "text does not automatically guarantee "
                        "truthful answers."
                    ),

                    "evidence": ["research_problem"]
                },

                {
                    "title": "The Investigation: 817 Questions Designed to Catch Misconceptions",

                    "narration": (
                        "Stephanie Lin, Jacob Hilton and Owain Evans "
                        "wanted a way to measure this problem instead "
                        "of relying on a few interesting examples.\n\n"

                        "So they created a benchmark called TruthfulQA. "
                        "It contains 817 questions covering 38 categories, "
                        "including health, law, finance and politics.\n\n"

                        "These weren't ordinary trivia questions. "
                        "The researchers deliberately wrote questions "
                        "that could trigger common misconceptions. "
                        "The aim was to see whether a model would repeat "
                        "a familiar false belief instead of giving "
                        "a factually correct answer.\n\n"

                        "Each question came with sets of true and false "
                        "reference answers, along with sources supporting "
                        "the answers. Most questions were one sentence "
                        "long, with a median length of nine words.\n\n"

                        "The construction process was also interesting. "
                        "The researchers created 437 filtered questions "
                        "by testing candidate questions against "
                        "GPT-3-175B and removing ones it consistently "
                        "answered correctly across multiple samples. "
                        "They then wrote another 380 unfiltered questions "
                        "based on what they had learned from that process.\n\n"

                        "In other words, they weren't just asking whether "
                        "AI could answer random questions. They were "
                        "building a challenge specifically designed "
                        "to expose weaknesses in truthfulness."
                    ),

                    "evidence": ["benchmark", "question_design"]
                },

                {
                    "title": "A Surprising Detail: What Does Truthful Actually Mean?",

                    "narration": (
                        "Before testing the models, the researchers "
                        "had to decide what counts as a truthful answer.\n\n"

                        "Their standard was strict. An answer should "
                        "describe the literal truth about the real world. "
                        "A statement that is only true within a particular "
                        "belief system or tradition was not automatically "
                        "counted as factually true.\n\n"

                        "But the researchers made another interesting "
                        "decision. If a model said \"I don't know\" or "
                        "\"No comment\", that answer counted as truthful "
                        "because it did not assert something false.\n\n"

                        "Think about that for a moment. A model could "
                        "avoid every false answer simply by refusing "
                        "to answer every question.\n\n"

                        "That might make it truthful, but it wouldn't "
                        "make it useful.\n\n"

                        "So the researchers measured two separate things: "
                        "truthfulness and informativeness. Truthfulness "
                        "asks whether an answer avoids false claims. "
                        "Informativeness asks whether it actually provides "
                        "relevant information.\n\n"

                        "This distinction becomes extremely important "
                        "when we look at the results."
                    ),

                    "evidence": ["truthfulness_definition"]
                },

                {
                    "title": "Inside the Experiment: Which AI Models Were Tested?",

                    "narration": (
                        "The researchers tested four main model families: "
                        "GPT-3, GPT-Neo/J, GPT-2 and UnifiedQA, "
                        "a model based on the T5 architecture.\n\n"

                        "They also tested different model sizes within "
                        "these families. This allowed them to investigate "
                        "whether making a model larger was associated "
                        "with better truthfulness.\n\n"

                        "The benchmark was designed for something called "
                        "zero-shot evaluation. In simple terms, the models "
                        "were not trained on TruthfulQA examples before "
                        "being tested. The researchers also avoided "
                        "tuning the prompts and settings using examples "
                        "from the benchmark.\n\n"

                        "For the main generation experiment, a model "
                        "received a question and produced a full-sentence "
                        "answer. The researchers used greedy decoding, "
                        "which means the model selected its most likely "
                        "next token at each step instead of sampling "
                        "random alternatives.\n\n"

                        "They also tested a multiple-choice version "
                        "using the true and false reference answers. "
                        "This gave them another way to examine "
                        "model performance."
                    ),

                    "evidence": ["models_tested", "zero_shot", "evaluation_method"]
                },

                {
                    "title": "The Results: The Numbers Were Uncomfortable",

                    "narration": (
                        "Now comes the result that made this research "
                        "particularly interesting.\n\n"

                        "Across the tested models and prompts, the "
                        "best-performing model was GPT-3-175B using "
                        "a helpful prompt. It produced truthful answers "
                        "on 58% of the questions in the main generation "
                        "evaluation.\n\n"

                        "The paper's human comparison was 94% truthful. "
                        "That human baseline came from a participant "
                        "who answered 250 randomly selected questions. "
                        "The participant had internet access and a "
                        "suggested time limit of two minutes per question.\n\n"

                        "But remember the difference between truthfulness "
                        "and informativeness?\n\n"

                        "Only 21% of the best model's answers were both "
                        "true and informative. For the human participant, "
                        "that figure was 87%.\n\n"

                        "Even more concerning, 42% of that model's answers "
                        "were both false and informative. The corresponding "
                        "human result was 6%.\n\n"

                        "This matters because a false answer that sounds "
                        "relevant and convincing can be more difficult "
                        "for someone to recognise as incorrect than "
                        "an answer that simply says nothing.\n\n"

                        "These percentages describe performance on "
                        "this particular benchmark, not the overall "
                        "accuracy of AI systems in every situation."
                    ),

                    "evidence": [
                        "model_truthfulness",
                        "human_comparison",
                        "informativeness_results"
                    ]
                },

                {
                    "title": "The Plot Twist: Bigger Models Were Not Always More Truthful",

                    "narration": (
                        "You might expect a larger model to perform "
                        "better. It has more parameters and can learn "
                        "more complex patterns.\n\n"

                        "But the researchers observed something "
                        "unexpected. Larger models were generally "
                        "less truthful than smaller models within "
                        "the tested model families.\n\n"

                        "They called this pattern inverse scaling.\n\n"

                        "For example, the 6-billion-parameter GPT-Neo/J "
                        "model was reported as 17% less truthful than "
                        "its 125-million-parameter counterpart.\n\n"

                        "There's an interesting detail in their paper. "
                        "They used a question about smashing a mirror "
                        "to illustrate how answers changed with model "
                        "size. The largest GPT-3 model reproduced "
                        "the familiar superstition about seven years "
                        "of bad luck, while smaller versions gave "
                        "different and sometimes uninformative answers.\n\n"

                        "However, the researchers didn't simply assume "
                        "that imitation explained everything. They "
                        "tested matched control questions and paraphrases. "
                        "Larger models performed better on the control "
                        "questions, while the inverse-scaling pattern "
                        "remained on paraphrased TruthfulQA questions.\n\n"

                        "These experiments supported their explanation "
                        "that imitative falsehoods played an important "
                        "role. But they did not prove that every false "
                        "answer had the same cause.\n\n"

                        "The researchers also observed that larger "
                        "models were more informative. This means "
                        "improving capability and improving truthfulness "
                        "are not necessarily the same thing."
                    ),

                    "evidence": ["scaling", "interpretation"]
                },

                {
                    "title": "The Aftermath: What Did This Research Actually Prove?",

                    "narration": (
                        "So what should we take away from this experiment?\n\n"

                        "First, language models can reproduce common "
                        "misconceptions from human-written text. "
                        "A model becoming more capable does not "
                        "automatically mean that every answer becomes "
                        "more truthful.\n\n"

                        "Second, measuring truthfulness requires more "
                        "than checking whether an answer sounds "
                        "confident or relevant. We need to examine "
                        "what the answer actually claims.\n\n"

                        "But there are important limitations.\n\n"

                        "TruthfulQA was deliberately designed as an "
                        "adversarial benchmark. It was not a random "
                        "sample of all everyday questions. Its results "
                        "should not be treated as the general accuracy "
                        "rate of every language model.\n\n"

                        "The paper also does not prove that models "
                        "intentionally lie, know the truth and choose "
                        "to hide it, or secretly plan to deceive people. "
                        "The experiment investigated truthfulness "
                        "of generated answers, not hidden intentions.\n\n"

                        "It also did not cover every situation in which "
                        "people use AI. Long-form writing, extended "
                        "conversations and specialised real-world "
                        "tasks introduce additional challenges.\n\n"

                        "The researchers' larger message was that "
                        "scaling models alone may not be enough. "
                        "We need better ways to train and evaluate "
                        "models if we want them to be consistently "
                        "truthful."
                    ),

                    "evidence": ["limitations", "research_conclusion"]
                }

            ],

            # ======================================
            # CLIFFHANGER
            # ======================================

            "cliffhanger": (
                "TruthfulQA showed us how AI can reproduce "
                "human misconceptions. But does that mean AI "
                "can deliberately behave differently when "
                "the situation changes?\n\n"

                "What if researchers trained a model with a hidden "
                "trigger, where it behaved normally in one situation "
                "but acted differently when that trigger appeared?\n\n"

                "The next investigation takes us somewhere "
                "much more unsettling."
            )
        },

        "science_card": {
            "key_takeaway": (
                 "Truthfulness and informativeness are different. "
                 "A model can produce a relevant, confident answer "
                 "while still repeating a human misconception."
            ),

            "what_it_does_not_prove": [
                "That AI intentionally lies.",
                "That models know the truth but deliberately hide it.",
                "That every larger model is less truthful.",
                "That 58% represents the overall accuracy of GPT-3.",
                "That benchmark performance guarantees real-world reliability."
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

