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
    },

    "toy-models-superposition-2022":{
        "title": "Toy Models of Superposition",

        "authors": [
            "Nelson Elhage",
            "Tristan Hume",
            "Catherine Olsson",
            "Nicholas Schiefer",
            "Tom Henighan",
            "Shauna Kravec",
            "Zac Hatfield-Dodds",
            "Robert Lasenby",
            "Dawn Drain",
            "Carol Chen",
            "Roger Grosse",
            "Sam McCandlish",
            "Jared Kaplan",
            "Dario Amodei",
            "Martin Wattenberg",
            "Christopher Olah"
        ],

        "year": 2022,
        "venue": "Transform Circuits Thread",

        "source": {
            "url" : "https://transformer-circuits.pub/2022/toy_model/index.html",
            "arxiv": "https://arxiv.org/abs/2209.10652"
        },

        "research": {
            "question":(
                "How can neural networks represent more features "
                "than they have dimensions, and what trade-offs "
                "does this create?"
            ),

            "problem": (
                "Individual neurons do not always correspond to "
                "one clean, understandable concept. Some appear "
                "to respond to multiple seemingly unrelated features. "
                "This makes understanding internal representations "
                "more difficult."
            ),

            "experiment": {
                "model_families": [
                    "Small ReLU networks",
                    "Networks trained on synthetic sparse features"
                ]
            },

            "findings": [
                {
                    "id": "superposition",

                    "result": "More features than dimensions",

                    "meaning": (
                        "The ReLU toy models can represent more "
                        "features than available hidden dimensions "
                        "when the features are sufficiently sparse. "
                        "They achieve this by representing features "
                        "in overlapping, non-orthogonal directions."
                    ),

                    "source_location": (
                         "Abstract and Demonstrating Superposition"
                    )
                },

                {
                    "id":  "sparsity",
                    "result": "Sparsity makes compression useful",
                    "meaning": (
                        "When features are sparse, they are less "
                        "likely to activate together. This can make "
                        "the benefit of representing extra features "
                        "worth the interference introduced by "
                        "overlapping representations."
                    ),

                    "source_location": (
                        "Background and Mathematical Understanding"
                    )

                },

                {
                    "id": "interference",
                    "result": "Superposition has a cost",
                    "meaning": (
                        "Features represented in non-orthogonal "
                        "directions can interfere with one abother. "
                        "The ReLU nonlinearity and bias can help "
                        "filter some small amounts of interference, "
                        "but the representations are not perfectly "
                        "independent."
                    ),

                    "source_location":(
                        "The Superposition Hypothesis and "
                        "Mathematical Understanding"
                    )
                },

                {
                    "id": "phase-change",
                    "result": "Different representation regimes",
                    "meaning": (
                        "A feature may remain unlearned, receive "
                        "a dedicated dimension, or be represented. "
                        "in superposition, The researchers observed "
                        "sharp transitions between these strategies "
                        "as sparsity and relative feature importance "
                        "changed."
                    ),
                    
                    "source_location": (
                        "Superposition as a Phase Change"
                    )
                },
                
                {
                    "id": "geometry",

                    "result": "Structured geometric arrangements",

                    "meaning": (
                        "In uniform superposition experiments, "
                        "feature directions organized into geometric "
                        "structures such as antipodal pairs, triangles, "
                        "pentagons and tetrahedra."
                    ),
                    "source_location": (
                        "The Geometry of Superposition"
                    )

                }
            ],

            "limitations": [
                (
                    "The experiments use small ReLU networks "
                    "and synthetic data, rather than a deployed "
                    "large language model."
                ),
                (
                "The authors explicitly state that it was unclear "
                "how much of the observed behaviour generalizes "
                "to real neural networks." 
                ),
                (
                "The geometric structures may be partly "
                "specific to the simplified toy models."
                ),

                (
                    "The paper notes that the theory of non-uniform "
                    "superposition is still incomplete."
                ),

                (
                    "The experiments do not provide a complete "
                    "explanation of the internal representations "
                    "or decisions of a production language model."
                )
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

    },

    "inside-black-box-ep01":{

        "id": "inside-black-box-ep01",

        "paper_id": "toy-models-superposition-2022",

        "series_id": "inside-black-box",

        "episode_number": 1,

        "presentation": {

            "title": "The Neuron That Means Too Many Things",

            "tagline": (
                "One tiny network. More features than dimensions. "
                "A hidden cost."
            ),

            "genre": "Scientific Thriller",

            "difficulty": "Beginner",

            "estimated_minutes": 9,

            "thumbnail": {
                "headline": "ONE NEURON. TOO MANY CONCEPTS?",
                "visual": (
                    "A mysterious neural network with overlapping "
                    "representations hidden inside its layers"
                )
            }
        },

        "story": {

            "cold_open": (

                "Imagine a tiny room with only two spaces available.\n\n"

                "Now imagine five different things trying to fit "
                "inside that room. Five signals. Five pieces of "
                "information. But only two dimensions to store them.\n\n"

                "The obvious solution seems simple: choose the "
                "two most important things and forget the rest.\n\n"

                "But what if a neural network found another way?\n\n"

                "What if it could squeeze more information into "
                "less space by allowing different features to "
                "share overlapping directions?\n\n"

                "That sounds clever. Almost impossible.\n\n"

                "And it raises a strange question: what if the "
                "neurons we are trying to understand are not "
                "representing just one clean concept?\n\n"

                "In 2022, a group of researchers built a tiny "
                "experimental world to investigate exactly this "
                "possibility. What they found was a phenomenon "
                "they called superposition."
            ),
            #CHAPTER 1 

            "chapters":[
                {
                    "title": (
                        "The Neuron Problem: "
                        "Why One Neuron Isn't Always One Feature"
                    ),

                    "narration": (
                        "Let's begin with a simple assumption.\n\n"

                        "Suppose we open a neural network and find "
                        "a neuron that responds whenever a certain "
                        "visual pattern appears. We might describe "
                        "it as a feature detector.\n\n"

                        "A feature is simply a property or pattern "
                        "in the input that the network can represent. "
                        "It could be something visual, a word-related "
                        "pattern, or a much more abstract property.\n\n"

                        "This is the picture we would love to have: "
                        "one neuron, one understandable feature. "
                        "Researchers often call this kind of clean "
                        "alignment monosemantic behaviour.\n\n"

                        "But neural networks do not always behave "
                        "so neatly.\n\n"

                        "Some neurons appear to respond to several "
                        "different features. A single activation "
                        "might be associated with patterns that "
                        "do not seem closely related to us.\n\n"

                        "This is often described as polysemanticity.\n\n"

                        "The problem is obvious. If one neuron "
                        "responds to several features, simply "
                        "looking at that neuron's activation may "
                        "not tell us exactly what information "
                        "the network is representing.\n\n"

                        "The researchers explored a possible "
                        "explanation: perhaps the network is "
                        "trying to represent more features than "
                        "it has dimensions available.\n\n"

                        "But how could that even work?"
                    ),

                    "evidence": [
                        "feature-representations",
                        "polysemanticity"
                    ]
                },

                #CHAPTER 2 

                {
                    "title": (
                        "The Experiment: "
                        "A Tiny Lab With Five Features and Two Dimensions"
                    ),

                    "narration": (
                        "Instead of beginning with a giant language "
                        "model, the researchers built something "
                        "much smaller and easier to study.\n\n"

                        "Think of an artificial world containing "
                        "five input features. The network has only "
                        "two hidden dimensions available to represent "
                        "them.\n\n"

                        "The researchers created synthetic data "
                        "for these features. Each feature could "
                        "sometimes be zero and otherwise take "
                        "a value between zero and one.\n\n"

                        "The probability of a feature being zero "
                        "controlled its sparsity. A feature that "
                        "appeared only occasionally was considered "
                        "more sparse.\n\n"

                        "The network had a simple job. First, "
                        "compress the high-dimensional input into "
                        "a smaller hidden representation. Then "
                        "attempt to reconstruct the original input.\n\n"

                        "The researchers compared two approaches.\n\n"

                        "The first was a linear model. The second "
                        "used a ReLU output activation.\n\n"

                        "Why was that small difference important?\n\n"

                        "Because adding that nonlinearity changed "
                        "what the model could learn. The linear "
                        "baseline generally selected the most "
                        "important features it could fit in its "
                        "available dimensions.\n\n"

                        "The ReLU model opened the door to something "
                        "more surprising.\n\n"

                        "The experiment was not a test of a real "
                        "commercial language model. It was a "
                        "controlled environment designed to "
                        "understand one possible mechanism "
                        "behind neural representations."
                    ),

                    "evidence": [
                        "synthetic-data",
                        "relu-experiment"
                    ]
                },

                #CHAPTER 3 

                {
                   "title": (
                        "The Results: "
                        "Five Features. Two Dimensions."
                    ),

                    "narration": (

                        "Now comes the surprising part.\n\n"

                        "In an ordinary linear model, representing "
                        "more features than available dimensions "
                        "creates a difficult trade-off. The model "
                        "usually keeps the most important features "
                        "and leaves the others out.\n\n"

                        "But the ReLU output model behaved "
                        "differently when the input features "
                        "became sparse.\n\n"

                        "Instead of giving every feature its own "
                        "separate dimension, the network could "
                        "represent several features using directions "
                        "that were not perfectly orthogonal.\n\n"

                        "Imagine drawing several arrows inside "
                        "the same two-dimensional space. If every "
                        "arrow had to be at a right angle to every "
                        "other arrow, we could fit only two "
                        "independent directions.\n\n"

                        "But the network did not require perfect "
                        "right angles. It could use directions "
                        "that were close to orthogonal while "
                        "sharing the same limited space.\n\n"

                        "This is the central idea of superposition: "
                        "representing more features than there "
                        "are dimensions available.\n\n"

                        "The researchers demonstrated this in "
                        "their toy models. They also studied larger "
                        "configurations, including 80 input features "
                        "represented using 20 hidden dimensions.\n\n"

                        "But there was a catch.\n\n"

                        "The extra information did not come for "
                        "free. Sharing the same representational "
                        "space created interference."
                    ),

                    "evidence": [
                        "superposition",
                        "sparsity"
                    ]
                },

                #CHAPTER 4 

                {
                    "title": (
                        "The Hidden Cost: "
                        "Interference Is the Price"
                    ),

                    "evidence": [
                        "interference"
                    ]
                },

                #CHAPTER 5

                {
                   "title": (
                        "The Turning Point: "
                        "A Phase Change in Representation" 
                    ),

                    "narration": (

                        "The researchers discovered that "
                        "superposition was not simply an "
                        "all-or-nothing decision.\n\n"

                        "Depending on the conditions, a feature "
                        "could fall into one of three broad "
                        "situations.\n\n"

                        "First, the network might not learn "
                        "the feature at all.\n\n"

                        "Second, it might represent the feature "
                        "in superposition, sharing representational "
                        "space with other features.\n\n"

                        "Or third, it might give that feature "
                        "a dedicated dimension.\n\n"

                        "To investigate these transitions, "
                        "the researchers changed two important "
                        "variables: how sparse the features were "
                        "and how important one feature was "
                        "relative to another.\n\n"

                        "They observed sharp transitions between "
                        "different representation strategies.\n\n"   

                        "The paper calls this a phase change.\n\n"

                        "There is an important detail here. "
                        "The authors use that term in a generalized "
                        "sense, meaning a discontinuous change "
                        "between regimes. They are not claiming "
                        "that a neural network literally undergoes "
                        "a physical phase transition like water "
                        "turning into ice.\n\n"

                        "It means that a gradual change in "
                        "experimental conditions can sometimes "
                        "lead to a sudden change in the network's "
                        "preferred representation."
                        
                        ),

                        "evidence": [
                        "phase-change"
                    ]       
                },

                #CHAPTER 6 

                {
                   "title": (
                        "The Geometry: "
                        "A Hidden Architecture of Shapes"
                    ),

                    "narration": (

                        "There was another unexpected discovery.\n\n"

                        "When the researchers examined how "
                        "features were arranged in their toy "
                        "models, they found that the directions "
                        "were not always scattered randomly.\n\n"

                        "In experiments with uniform features, "
                        "the directions could form recognisable "
                        "geometric structures.\n\n"

                        "Some appeared as antipodal pairs: "
                        "two feature directions pointing in "
                        "exactly opposite directions.\n\n"

                        "Other configurations involved triangles, "
                        "pentagons and tetrahedra.\n\n"

                        "The paper also discusses more complicated "
                        "structures, including square antiprisms.\n\n"

                        "Why should geometry appear in a neural "
                        "network experiment?\n\n"

                        "Because each feature is represented "
                        "by a direction in the hidden space. "
                        "The angles between those directions "
                        "influence how much the features interfere "
                        "with one another.\n\n"

                        "The model is effectively balancing "
                        "two competing pressures: represent "
                        "useful features, while reducing the "
                        "interference between them.\n\n"

                        "The researchers found that this problem "
                        "has a surprising relationship with "
                        "geometric point-packing problems.\n\n"

                        "But they were careful about the "
                        "interpretation. They noted that these "
                        "elegant geometric structures could "
                        "be partly specific to the simplified "
                        "toy model they studied.\n\n"

                        "The real world may be much less tidy."

                    ),

                    "evidence": [
                        "geometry"
                    ]
                },

                # CHAPTER 7

                {
                    "title": (
                        "The Aftermath: "
                        "What This Toy Model Does—and Doesn't—Show"
                    ),

                    "narration": (

                        "So what did the researchers actually "
                        "establish?\n\n"

                        "They demonstrated that small neural "
                        "networks can represent more features "
                        "than available dimensions under "
                        "specific experimental conditions.\n\n"

                        "They showed how sparsity can make "
                        "this strategy useful, why interference "
                        "appears, and how different representation "
                        "regimes can emerge.\n\n"

                        "They also uncovered unexpectedly "
                        "structured geometry in their toy models.\n\n"

                        "But we need to be careful about what "
                        "we conclude.\n\n"

                        "These experiments used small ReLU "
                        "networks and synthetic data. They did "
                        "not directly demonstrate the same "
                        "mechanism inside a deployed large "
                        "language model.\n\n"

                        "The authors explicitly acknowledge "
                        "that it is unclear how much of the "
                        "observed behaviour generalizes to "
                        "real neural networks.\n\n"

                        "They also point out that real-world "
                        "superposition is likely to be "
                        "non-uniform, with features differing "
                        "in importance, sparsity and correlation.\n\n"

                        "So this paper does not solve the "
                        "entire problem of understanding "
                        "a neural network.\n\n"

                        "What it gives us is something "
                        "extremely valuable: a possible "
                        "mechanism that researchers can "
                        "investigate more deeply.\n\n"


                        "And that leads to a much bigger "
                        "question."

                    ),

                    "evidence": [
                        "limitations"
                    ]
                }
            ],

            #CLIFFHANGER

            "cliffhanger": (

                "We have seen how a tiny neural network can "
                "represent more features than it has dimensions.\n\n"

                "But so far, everything has happened inside "
                "a controlled toy experiment.\n\n"

                "What happens when we leave this tiny laboratory "
                "and look inside a real language model?\n\n"

                "Can researchers identify the individual features "
                "hidden inside its enormous activation spaces?\n\n"

                "And if many features are packed together, "
                "is there a way to separate them again?\n\n"

                "The next investigation moves beyond toy networks "
                "and into the search for interpretable features "
                "inside real language models."
            )
        },

        #SCIENCE CARD

        "science_card": {

            "key_takeaway": (
                "Superposition is a way for a neural network "
                "to represent more features than it has "
                "dimensions. Sparsity can make this useful, "
                "but overlapping representations introduce "
                "interference."
            ),

            "what_it_does_not_prove": [

                "That every neuron in a production language model is polysemantic.",

                "That the same geometric structures occur in every neural network.",

                "That the toy-model mechanism fully explains the internal representations of large language models.",

                "That superposition is always beneficial or always used.",

                "That researchers have completely solved the problem of interpreting neural networks."
            ]

        },

        "navigation": {
            "next_episode_id": None,
            "previous_episode_id": None
        },

        "publication_status": "published"
},

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
    },

    "inside-black-box": {

        "id": "inside-black-box",

        "title": "Inside the Black Box",

        "description": (
            "An investigation into the hidden representations "
            "inside neural networks, polysemanticity, "
            "superposition and mechanistic interpretability."
        ),

        "genre": "Scientific Thriller",

        "topic": "Mechanistic Interpretability",

        "cover": {
            "headline": "WHAT IS HAPPENING INSIDE AI?",
            "visual": ("A hidden neural world filled with overlapping "
                "features and mysterious representations"
            )
        },

        "episode_ids": [
            "inside-black-box-ep01"
        ],

        "status": "published"

    }
}

