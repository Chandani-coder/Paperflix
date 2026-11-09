
/* =========================================
   PAPERFLIX — FRONTEND APPLICATION
========================================= */

const API = "/api";

const FEATURED_SERIES_ID = "ai-that-lies";

const SERIES_ARTWORK = {
    "ai-that-lies": "/static/images/series-ai-lies.jpg"
};

const EPISODE_ARTWORK = {
    "truthfulqa-ep01": "/static/images/episode-truthfulqa.jpg"
};


// =========================================
// 1. SESSION MANAGEMENT
// =========================================

function getSessionId() {
    let sessionId = localStorage.getItem("paperflix_session_id");

    if (!sessionId) {
        sessionId = crypto.randomUUID
            ? crypto.randomUUID()
            : `paperflix-${Date.now()}`;

        localStorage.setItem("paperflix_session_id", sessionId);
    }

    return sessionId;
}

const SESSION_ID = getSessionId();


// =========================================
// 2. API HELPER
// =========================================

async function apiRequest(endpoint, options = {}) {

    const response = await fetch(`${API}${endpoint}`, {
        ...options,
        headers: {
            "Content-Type": "application/json",
            ...options.headers
        }
    });

    const data = await response.json();

    if (!response.ok) {
        throw new Error(
            data.detail || "Something went wrong!"
        );
    }

    return data;
}


// =========================================
// 3. HTML SAFETY
// =========================================

function escapeHTML(value) {
    return String(value ?? "").replace(/[&<>"']/g, char => ({
        "&": "&amp;",
        "<": "&lt;",
        ">": "&gt;",
        '"': "&quot;",
        "'": "&#39;"
    })[char]);
}


// =========================================
// 4. LOAD SERIES
// =========================================

async function loadSeries() {

    const container = document.getElementById("series-list");

    if (!container) {
        console.error("Series catalogue container #series-list was not found.");
        return;
    }

    // Planned catalogue entries. These are display-only until real
    // series and episodes are added to the backend.
    const upcomingSeries = [
        {
            id: "inside-black-box",
            title: "Inside the Black Box",
            topic: "MECHANISTIC INTERPRETABILITY",
            genre: "AI Safety",
            subtitle: "What is really happening inside an AI model?",
            image: "/static/images/inside-blackbox.png",
            artworkClass: "blackbox"
        },
        {
            id: "reward-trap",
            title: "The Reward Trap",
            topic: "REWARD HACKING",
            genre: "AI Safety",
            subtitle: "What happens when AI learns to game its reward?",
            image: "/static/images/reward-trap.png",
            artworkClass: "reward"
        },
        {
            id: "can-ai-be-fooled",
            title: "Can AI Be Fooled?",
            topic: "ADVERSARIAL ROBUSTNESS",
            genre: "AI Safety",
            subtitle: "How easily can intelligent systems be manipulated?",
            image: "/static/images/adversarial-ai.jpg",
            artworkClass: "fooled"
        },
        {
            id: "watchers",
            title: "Who Watches the Watchers?",
            topic: "AI EVALUATION",
            genre: "AI Safety",
            subtitle: "Who checks whether an AI system is actually safe?",
            image: "/static/images/ai-oversight.png",
            artworkClass: "watchers"
        },
        {
            id: "agents-collude",
            title: "When Agents Collude",
            topic: "MULTI-AGENT ALIGNMENT",
            genre: "AI Safety",
            subtitle: "What happens when AI agents start cooperating?",
            image: "/static/images/agent-collusion.webp",
            artworkClass: "collude"
        }
    ];

    container.innerHTML = "";

    let publishedSeries = [];

    // Load published series from the backend.
    try {
        const response = await apiRequest("/series");

        if (Array.isArray(response.series)) {
            publishedSeries = response.series.filter(
                series => series && series.id
            );
        } else {
            console.warn(
                "The /series endpoint did not return a series array:",
                response
            );
        }

    } catch (error) {
        console.error(
            "Published series list could not be loaded:",
            error
        );
    }

    // Make sure the featured series is present in the catalogue.
    // If it is missing from the list endpoint, try its detail endpoint.
    const featuredIsListed = publishedSeries.some(
        series => series.id === FEATURED_SERIES_ID
    );

    if (!featuredIsListed) {
        try {
            const featuredResponse = await apiRequest(
                `/series/${encodeURIComponent(FEATURED_SERIES_ID)}`
            );

            const featuredSeries =
                featuredResponse.series || featuredResponse;

            if (
                featuredSeries &&
                featuredSeries.id === FEATURED_SERIES_ID
            ) {
                publishedSeries.push(featuredSeries);
            } else {
                console.warn(
                    "Featured series detail response did not contain the expected series id:",
                    featuredResponse
                );
            }

        } catch (error) {
            console.error(
                "Featured series was not available from the detail endpoint:",
                error
            );
        }
    }

    // Remove duplicates and put the featured playable series first.
    const uniqueSeries = Array.from(
        new Map(
            publishedSeries.map(series => [series.id, series])
        ).values()
    );

    uniqueSeries.sort((a, b) => {
        if (a.id === FEATURED_SERIES_ID) return -1;
        if (b.id === FEATURED_SERIES_ID) return 1;
        return 0;
    });

    // Render real, published series first.
    uniqueSeries.forEach(series => {

        const card = document.createElement("article");

        card.className = "series-card published-series-card";
        card.dataset.seriesId = series.id;
        card.tabIndex = 0;
        card.setAttribute("role", "button");
        card.setAttribute("aria-label", `Open ${series.title}`);

        const artwork = SERIES_ARTWORK[series.id] || "";

        const hasEpisodeCount =
            series.episode_count !== undefined &&
            series.episode_count !== null &&
            series.episode_count !== "" &&
            Number.isFinite(Number(series.episode_count));

        const episodeCount = hasEpisodeCount
            ? Number(series.episode_count)
            : Array.isArray(series.episodes)
                ? series.episodes.length
                : null;

        const episodeMeta = episodeCount === null
            ? "Research Series"
            : `${episodeCount} ${episodeCount === 1 ? "Episode" : "Episodes"}`;

        card.innerHTML = `
            <div class="poster catalog-poster">

                ${artwork ? `
                    <img
                        class="poster-image"
                        src="${escapeHTML(artwork)}"
                        alt="${escapeHTML(series.title)}"
                        loading="lazy"
                    >
                ` : ""}

                <div class="catalog-poster-shade"></div>

                <span class="catalogue-status available-status">
                    AVAILABLE
                </span>

            </div>

            <div class="card-information">
                <h3>${escapeHTML(series.title)}</h3>
                <p>
                    ${escapeHTML(series.genre || "AI Safety")}
                    · ${escapeHTML(episodeMeta)}
                </p>
            </div>
        `;

        const openSelectedSeries = () => openSeries(series.id);

        card.addEventListener("click", openSelectedSeries);

        card.addEventListener("keydown", event => {
            if (event.key === "Enter" || event.key === " ") {
                event.preventDefault();
                openSelectedSeries();
            }
        });

        container.appendChild(card);
    });

    // Make a missing featured series visible instead of silently hiding it.
    if (!uniqueSeries.some(
        series => series.id === FEATURED_SERIES_ID
    )) {
        const warning = document.createElement("p");

        warning.className = "series-load-warning";
        warning.textContent =
            "The featured series could not be loaded. Please check the backend series API.";

        container.appendChild(warning);
    }

    // Render upcoming catalogue entries.
    // These are intentionally not clickable.
    upcomingSeries.forEach(series => {

        const card = document.createElement("article");

        card.className = "series-card upcoming-card";
        card.dataset.seriesId = series.id;

        card.innerHTML = `
            <div class="poster upcoming-poster">

                <img
                    class="upcoming-poster-image"
                    src="${escapeHTML(series.image)}"
                    alt="${escapeHTML(series.title)}"
                    loading="lazy"
                    onerror="this.style.display='none'"
                >

                <div class="catalog-poster-shade"></div>

                <span class="catalogue-status">
                    COMING SOON
                </span>

            </div>

            <div class="card-information">
                <h3>${escapeHTML(series.title)}</h3>

                <p>
                    ${escapeHTML(series.genre)} · Upcoming
                </p>

                <p class="upcoming-description">
                    ${escapeHTML(series.subtitle)}
                </p>
            </div>
        `;

        // No click handler: unpublished series cannot be opened.
        container.appendChild(card);
    });
}


// =========================================
// 5. LOAD EPISODES FOR A SELECTED SERIES
// =========================================

async function loadEpisodes(seriesId, seriesData = null) {

    const container = document.getElementById("episode-list");
    const section = document.getElementById("episodes");

    if (!container || !section) {
        console.error("Episode section elements not found.");
        return;
    }

    try {

        // Reuse series data if openSeries() already fetched it.
        const series = seriesData || await apiRequest(
            `/series/${encodeURIComponent(seriesId)}`
        );

        const episodes = Array.isArray(series.episodes)
            ? series.episodes
            : [];

        // Reveal and update the selected series section.
        section.hidden = false;

        const heading = document.getElementById("episode-section-title");

        const description = document.getElementById(
            "episode-section-description"
        );

        if (heading) {
            heading.textContent = series.title || "Series Episodes";
        }

        if (description) {
            description.textContent =
                `Explore the research investigations in ${series.title || "this series"}.`;
        }

        container.innerHTML = "";

        // Handle a series that has no published episodes.
        if (episodes.length === 0) {

            container.innerHTML = `
                <div class="empty-episodes">
                    <h3>No episodes published yet.</h3>
                    <p>
                        This research series is being prepared.
                        Check back for the next investigation.
                    </p>
                </div>
            `;

            section.scrollIntoView({
                behavior: "smooth",
                block: "start"
            });

            return;
        }

        // Render the published episodes.
        episodes.forEach(episode => {

            const card = document.createElement("article");

            card.className = "episode-card";
            card.dataset.episodeId = episode.id;

            const thumbnailText =
                episode.thumbnail?.headline || episode.title;

            const artwork = EPISODE_ARTWORK[episode.id] || "";

            card.innerHTML = `
                <div class="episode-art episode-truth">

                    ${artwork ? `
                        <img
                            class="episode-image"
                            src="${artwork}"
                            alt=""
                            loading="lazy"
                        >
                    ` : ""}

                    <div class="episode-shade"></div>

                    <span class="episode-number">
                        ${String(episode.episode_number).padStart(2, "0")}
                    </span>

                    <div class="episode-art-title">
                        ${escapeHTML(thumbnailText)}
                    </div>

                    <span class="episode-duration">
                        ${episode.estimated_minutes || 3} MIN
                    </span>

                </div>

                <div class="episode-information">

                    <span>
                        EPISODE ${episode.episode_number}
                    </span>

                    <h3>${escapeHTML(episode.title)}</h3>

                    <p>${escapeHTML(episode.tagline || "")}</p>

                </div>
            `;

            card.addEventListener("click", () => {
                openEpisode(episode.id);
            });

            container.appendChild(card);
        });

        // Bring the selected series' episodes into view.
        section.scrollIntoView({
            behavior: "smooth",
            block: "start"
        });

    } catch (error) {

        console.error("Episode loading failed:", error);

        container.innerHTML = `
            <p class="episode-error">
                Unable to load episodes. Please try again.
            </p>
        `;
    }
}


// =========================================
// 6. OPEN A SERIES
// =========================================

async function openSeries(seriesId) {

    try {

        const series = await apiRequest(
            `/series/${encodeURIComponent(seriesId)}`
        );

        // Show this series' episodes instead of automatically
        // starting its first episode.
        await loadEpisodes(seriesId, series);

    } catch (error) {

        console.error("Series loading failed:", error);

        alert(error.message || "Unable to open this series.");
    }
}


// =========================================
// 7. READER STYLES
// =========================================

function createReaderStyles() {

    if (document.getElementById("reader-styles")) return;

    const style = document.createElement("style");

    style.id = "reader-styles";

    style.textContent = `
        #episode-reader {
            position: fixed;
            inset: 0;
            z-index: 1000;
            background: rgba(0,0,0,0.97);
            overflow-y: auto;
            color: white;
            padding: 30px 20px;
        }

        .reader-container {
            max-width: 850px;
            margin: 35px auto;
        }

        .reader-top {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 45px;
        }

        .reader-brand {
            color: #e50914;
            font-size: 21px;
            font-weight: 900;
        }

        .reader-close {
            background: #252525;
            color: white;
            border: none;
            padding: 10px 16px;
            border-radius: 5px;
            cursor: pointer;
        }

        .reader-label {
            color: #e50914;
            font-size: 11px;
            font-weight: 900;
            letter-spacing: 2px;
        }

        .reader-title {
            font-size: clamp(30px, 6vw, 54px);
            line-height: 1.1;
            margin: 18px 0;
        }

        .reader-story {
            font-size: 18px;
            line-height: 1.9;
            color: #dedede;
            margin: 35px 0;
            white-space: pre-line;
        }

        .reader-progress {
            height: 4px;
            background: #333;
            border-radius: 10px;
            overflow: hidden;
            margin: 20px 0;
        }

        .reader-progress-fill {
            height: 100%;
            background: #e50914;
            transition: width 0.3s;
        }

        .reader-actions {
            display: flex;
            justify-content: space-between;
            gap: 12px;
            margin-top: 40px;
            flex-wrap: wrap;
        }

        .reader-actions button {
            padding: 13px 22px;
            border: none;
            border-radius: 5px;
            font-weight: bold;
            cursor: pointer;
        }

        .reader-next {
            background: #e50914;
            color: white;
        }

        .reader-previous {
            background: #292929;
            color: white;
        }

        .reader-source {
            display: block;
            color: #ff555d;
            margin-top: 30px;
            font-size: 13px;
        }

        .reader-source a {
            color: inherit;
            text-decoration: underline;
        }

        .reader-science {
            border-left: 3px solid #e50914;
            background: #181818;
            padding: 20px;
            margin-top: 35px;
            border-radius: 5px;
            color: #ccc;
            line-height: 1.7;
        }

        .reader-dots {
            color: #999;
            font-size: 12px;
            margin-top: 15px;
        }

        @media(max-width:600px) {
            .reader-story {
                font-size: 16px;
            }

            #episode-reader {
                padding: 20px 16px;
            }
        }
    `;

    document.head.appendChild(style);
}


// =========================================
// 8. SAVE READING PROGRESS
// =========================================

async function saveProgress(
    episodeId,
    progressPercent,
    completed = false
) {

    try {
        await apiRequest("/progress", {
            method: "PUT",

            body: JSON.stringify({
                session_id: SESSION_ID,
                episode_id: episodeId,
                progress_percent: progressPercent,
                completed: completed
            })
        });

    } catch (error) {
        console.error("Progress saving failed:", error);
    }
}


// =========================================
// 9. READER HELPERS
// =========================================

function getChapterType(index, chapter, total) {

    if (index === 0) return "opening";

    if (index === total - 1) return "cliffhanger";

    const title = (chapter.title || "").toLowerCase();

    if (/result|finding|numbers|plot twist/.test(title)) {
        return "results";
    }

    if (/aftermath|limitation|conclusion|prove/.test(title)) {
        return "aftermath";
    }

    if (/investigation|experiment|method|models|817/.test(title)) {
        return "investigation";
    }

    return "story";
}


function getChapterLabel(type) {

    const labels = {
        opening: "THE OPENING",
        story: "THE STORY",
        investigation: "INSIDE THE INVESTIGATION",
        results: "THE RESULTS",
        aftermath: "THE AFTERMATH",
        cliffhanger: "THE NEXT QUESTION"
    };

    return labels[type] || "THE INVESTIGATION";
}


function renderStoryParagraphs(content) {

    return String(content || "")
        .split(/\n\s*\n/)
        .map(paragraph => paragraph.trim())
        .filter(Boolean)
        .map(paragraph => `
            <p>${escapeHTML(paragraph).replace(/\n/g, "<br>")}</p>
        `)
        .join("");
}


// =========================================
// 10. RESEARCH VISUAL INSERTS
// =========================================

function renderResearchInsert(type, paper) {

    const research = paper.research || {};
    const experiment = research.experiment || {};

    // Investigation: show the actual study setup.

    if (type === "investigation") {

        const questions =
            experiment.questions ?? experiment.question_count;

        const categories =
            experiment.categories ?? experiment.category_count;

        const benchmark = experiment.benchmark;

        const stats = [
            {
                label: "BENCHMARK",
                value: benchmark
            },
            {
                label: "QUESTIONS",
                value: questions
            },
            {
                label: "CATEGORIES",
                value: categories
            }
        ].filter(item =>
            item.value !== undefined &&
            item.value !== null
        );

        const models =
            experiment.models_tested ||
            experiment.model_families ||
            [];

        if (!stats.length && !models.length) return "";

        return `
            <section class="research-insert">

                <div class="research-insert-label">
                    INSIDE THE EXPERIMENT
                </div>

                <div class="research-stats">

                    ${stats.map(item => `
                        <div class="research-stat">
                            <span>${escapeHTML(item.label)}</span>
                            <strong>${escapeHTML(item.value)}</strong>
                        </div>
                    `).join("")}

                </div>

                ${models.length ? `
                    <div class="research-models">
                        <h4>MODELS INCLUDED IN THE STUDY</h4>

                        <div class="research-tags">
                            ${models.map(model => `
                                <span>${escapeHTML(model)}</span>
                            `).join("")}
                        </div>
                    </div>
                ` : ""}

            </section>
        `;
    }


    // Results: show actual findings from the paper.

    if (type === "results") {

        const findings = research.findings || [];

        if (!findings.length) return "";

        return `
            <section class="research-insert">

                <div class="research-insert-label">
                    WHAT THE RESEARCH FOUND
                </div>

                <div class="research-findings">

                    ${findings.map(finding => `
                        <article class="research-finding">

                            <strong>
                                ${escapeHTML(finding.result ?? finding.claim ?? "Research finding")}
                            </strong>

                            <p>
                                ${escapeHTML(finding.meaning ?? finding.context ?? "")}
                            </p>

                        </article>
                    `).join("")}

                </div>

            </section>
        `;
    }


    // Aftermath: explain the study limitations.

    if (type === "aftermath") {

        const limitations = research.limitations || [];

        if (!limitations.length) return "";

        return `
            <section class="research-insert research-limitations">

                <div class="research-insert-label">
                    WHAT THIS STUDY DOES NOT ESTABLISH
                </div>

                <ul>
                    ${limitations.map(item => `
                        <li>${escapeHTML(item)}</li>
                    `).join("")}
                </ul>

            </section>
        `;
    }

    return "";
}


// =========================================
// 11. SCIENCE AND SOURCE CARDS
// =========================================

function renderEpisodeEvidence(episode, paper) {

    const science = episode.science_card || {};

    const sourceUrl =
        paper.source?.url ||
        paper.source?.paper_url ||
        paper.source?.arxiv;

    return `
        <section class="episode-evidence">

            <div class="research-insert">

                <div class="research-insert-label">
                    THE BIGGER PICTURE
                </div>

                <h3>What should you remember?</h3>

                <p>
                    ${escapeHTML(science.key_takeaway)}
                </p>

                ${science.what_it_does_not_prove?.length ? `
                    <h4>What this research does not prove</h4>

                    <ul>
                        ${science.what_it_does_not_prove.map(item => `
                            <li>${escapeHTML(item)}</li>
                        `).join("")}
                    </ul>
                ` : ""}

            </div>

            <div class="research-source-card">

                <span>THE ORIGINAL RESEARCH</span>

                <h3>${escapeHTML(paper.title)}</h3>

                <p>
                    ${escapeHTML((paper.authors || []).join(", "))}
                    · ${paper.year}
                    ${paper.venue ? ` · ${escapeHTML(paper.venue)}` : ""}
                </p>

                ${sourceUrl ? `
                    <a
                        href="${escapeHTML(sourceUrl)}"
                        target="_blank"
                        rel="noopener noreferrer">
                        Explore the original paper ↗
                    </a>
                ` : ""}

            </div>

        </section>
    `;
}


// =========================================
// 12. OPEN EPISODE — IMMERSIVE READER
// =========================================

async function openEpisode(episodeId) {

    try {

        const episode = await apiRequest(
            `/episodes/${encodeURIComponent(episodeId)}`
        );

        const story = episode.story;
        const paper = episode.paper;

        const sections = [
            {
                title: "The Opening",
                content: story.cold_open
            },

            ...(story.chapters || []).map(chapter => ({
                title: chapter.title,
                content: chapter.narration,
                evidence: chapter.evidence || []
            })),

            {
                title: "The Cliffhanger",
                content: story.cliffhanger
            }
        ];

        if (!sections.length || !paper) {
            throw new Error("Episode content is incomplete.");
        }

        let activeIndex = 0;

        // Restore previous reading position.
        try {

            const saved = await apiRequest(
                `/progress/${encodeURIComponent(SESSION_ID)}`
            );

            const progressItems = Array.isArray(saved.progress)
                ? saved.progress
                : [];

            const record = progressItems.find(
                item => item.id === episodeId
            );

            if (record && !record.completed) {

                activeIndex = Math.min(
                    sections.length - 1,
                    Math.max(
                        0,
                        Math.ceil(
                            record.progress_percent *
                            sections.length / 100
                        ) - 1
                    )
                );
            }

        } catch (error) {

            console.warn(
                "Could not restore reading progress:",
                error
            );
        }


        // Create reader.
        createReaderStyles();

        let modal = document.getElementById("episode-reader");

        if (!modal) {

            modal = document.createElement("div");
            modal.id = "episode-reader";

            modal.setAttribute("role", "dialog");
            modal.setAttribute("aria-modal", "true");

            modal.setAttribute(
                "aria-label",
                "PaperFlix research episode"
            );

            document.body.appendChild(modal);
        }

        modal.hidden = false;

        const artwork = EPISODE_ARTWORK[episode.id] || "";

        const nextEpisodeId =
            episode.navigation?.next_episode_id;

        function renderChapter() {

            const chapter = sections[activeIndex];

            const isOpening = activeIndex === 0;

            const isEnding =
                activeIndex === sections.length - 1;

            const chapterType = getChapterType(
                activeIndex,
                chapter,
                sections.length
            );

            const chapterLabel = getChapterLabel(chapterType);

            const progress = Math.round(
                ((activeIndex + 1) / sections.length) * 100
            );

            const nextButtonLabel = isEnding
                ? nextEpisodeId
                    ? "Next Investigation →"
                    : "Finish Episode ✓"
                : "Continue →";


            // Only show research breakdowns when relevant.
            const researchInsert = renderResearchInsert(
                chapterType,
                paper
            );


            // Source and takeaway appear only at the ending.
            const finalEvidence = isEnding
                ? renderEpisodeEvidence(episode, paper)
                : "";

            const episodeIntroduction = isOpening
                ? `
                    <section class="reader-episode-hero">

                        ${artwork ? `
                            <img
                                class="reader-hero-image"
                                src="${escapeHTML(artwork)}"
                                alt=""
                            >
                        ` : ""}

                        <div class="reader-hero-overlay"></div>

                        <div class="reader-hero-content">

                            <span class="reader-kicker">
                                PAPERFLIX ORIGINAL
                            </span>

                            <h1 class="reader-title">
                                ${escapeHTML(
                                    episode.presentation.title
                                )}
                            </h1>

                            <p>
                                ${escapeHTML(
                                    episode.presentation.tagline
                                )}
                            </p>

                            <div class="reader-episode-meta">
                                EPISODE ${episode.episode_number}
                                · ${escapeHTML(
                                    episode.presentation.difficulty || "Beginner"
                                )}
                                · ${episode.presentation.estimated_minutes || 5}
                                MIN READ
                            </div>

                        </div>

                    </section>
                `
                : `
                    <div class="reader-episode-context">
                        <span>AI THAT LIES? · EPISODE ${episode.episode_number}</span>

                        <h1>
                            ${escapeHTML(
                                episode.presentation.title
                            )}
                        </h1>
                    </div>
                `;


            const endingCard = isEnding
                ? `
                    <section class="reader-next-investigation">

                        <span class="reader-kicker">
                            ${nextEpisodeId
                                ? "THE INVESTIGATION CONTINUES"
                                : "END OF THIS INVESTIGATION"}
                        </span>

                        <h2>
                            ${nextEpisodeId
                                ? "READY FOR THE NEXT DISCOVERY?"
                                : "BUT THE QUESTIONS DON'T END HERE."}
                        </h2>

                        <p>
                            ${nextEpisodeId
                                ? "Another research investigation is waiting for you."
                                : "The next research investigation is being prepared. Your curiosity shouldn't stop here."}
                        </p>

                    </section>
                `
                : "";

            modal.innerHTML = `

                <div class="reader-container">

                    <!-- TOP BAR -->

                    <div class="reader-top">

                        <a href="/" class="reader-brand">
                            PaperFlix.
                        </a>

                        <button class="reader-close">
                            ✕ Close
                        </button>

                    </div>


                    <!-- EPISODE INTRODUCTION -->

                    ${episodeIntroduction}


                    <!-- READING PROGRESS -->

                    <section class="reader-main">

                        <div class="reader-progress-info">

                            <span>
                                ${chapterLabel}
                            </span>

                            <span>
                                CHAPTER ${activeIndex + 1}
                                OF ${sections.length}
                            </span>

                        </div>

                        <div class="reader-progress">
                            <div
                                class="reader-progress-fill"
                                style="width:${progress}%">
                            </div>
                        </div>

                        <p class="reader-progress-caption">
                            ${progress}% OF THIS INVESTIGATION EXPLORED
                        </p>


                        <!-- CHAPTER CONTENT -->

                        <div class="reader-chapter-header">

                            <span class="reader-kicker">
                                ${chapterLabel}
                            </span>

                            <h2 class="reader-chapter-title">
                                ${escapeHTML(chapter.title)}
                            </h2>

                        </div>


                        <article class="reader-story">
                            ${renderStoryParagraphs(chapter.content)}
                        </article>


                        <!-- RESEARCH VISUAL INSERT -->

                        ${researchInsert}


                        <!-- FINAL EPISODE MATERIAL -->

                        ${finalEvidence}

                        ${endingCard}


                        <!-- NAVIGATION -->

                        <div class="reader-actions">

                            <button
                                class="reader-previous"
                                ${activeIndex === 0 ? "disabled" : ""}>
                                ← Previous Chapter
                            </button>

                            <button class="reader-next">
                                ${nextButtonLabel}
                            </button>

                        </div>

                    </section>

                </div>
            `;


            modal.querySelector(
                ".reader-close"
            ).onclick = () => {

                modal.hidden = true;
                document.body.style.overflow = "";

                refreshContinue();
            };

            modal.querySelector(
                ".reader-previous"
            ).onclick = async () => {

                if (activeIndex > 0) {

                    activeIndex--;

                    const previousProgress = Math.round(
                        ((activeIndex + 1) / sections.length) * 100
                    );

                    await saveProgress(
                        episode.id,
                        previousProgress,
                        false
                    );

                    renderChapter();
                }
            };

            modal.querySelector(
                ".reader-next"
            ).onclick = async () => {

                if (!isEnding) {

                    activeIndex++;

                    const nextProgress = Math.round(
                        ((activeIndex + 1) / sections.length) * 100
                    );

                    await saveProgress(
                        episode.id,
                        nextProgress,
                        false
                    );

                    renderChapter();

                } else {

                    await saveProgress(
                        episode.id,
                        100,
                        true
                    );

                    // Fetch the next episode only when available.
                    const result = await apiRequest(
                        `/episodes/${encodeURIComponent(episode.id)}/next`
                    );

                    if (result.has_next) {

                        await openEpisode(
                            result.episode.id
                        );

                    } else {

                        modal.hidden = true;
                        document.body.style.overflow = "";

                        await refreshContinue();

                        alert(
                            "You've completed this investigation! " +
                            "The next episode is being prepared."
                        );
                    }
                }
            };


            // Save current chapter position.
            saveProgress(
                episode.id,
                progress,
                false
            );

            modal.scrollTop = 0;
        }

        document.body.style.overflow = "hidden";

        renderChapter();

    } catch (error) {

        console.error("Episode opening failed:", error);

        document.body.style.overflow = "";

        alert(error.message);
    }
}


// =========================================
// 13. CONTINUE WATCHING
// =========================================

async function refreshContinue() {

    const section = document.getElementById("continue");
    const container = document.getElementById("continue-list");

    if (!section || !container) {
        console.error("Continue Watching section elements were not found.");
        return;
    }

    try {

        const response = await apiRequest(
            `/progress/${encodeURIComponent(SESSION_ID)}`
        );

        const progressItems = Array.isArray(response.progress)
            ? response.progress
            : [];

        const unfinished = progressItems.filter(
            item => !item.completed &&
                Number(item.progress_percent) > 0
        );

        section.hidden = unfinished.length === 0;

        container.innerHTML = "";

        unfinished.forEach(item => {

            const card = document.createElement("article");

            card.className = "episode-card";

            card.innerHTML = `
                <div class="episode-art episode-truth">

                    <span class="episode-number">▶</span>

                    <div class="episode-art-title">
                        CONTINUE<br>YOUR STORY
                    </div>

                </div>

                <div class="episode-information">

                    <h3>${escapeHTML(item.title)}</h3>

                    <p>
                        ${item.progress_percent}% completed
                    </p>

                    <div class="reader-progress">
                        <div
                            class="reader-progress-fill"
                            style="width:${item.progress_percent}%">
                        </div>
                    </div>

                </div>
            `;

            card.onclick = () => openEpisode(item.id);

            container.appendChild(card);
        });

    } catch (error) {
        console.error("Continue Watching failed:", error);
    }
}


// =========================================
// 14. MY LIST
// =========================================

function setupMyList() {

    const button = document.getElementById("my-list");

    if (!button) return;

    let savedList = [];

    try {
        savedList = JSON.parse(
            localStorage.getItem("paperflix_my_list") || "[]"
        );

        if (!Array.isArray(savedList)) {
            savedList = [];
        }

    } catch (error) {
        console.error("Could not read My List:", error);
        savedList = [];
    }

    function updateButton() {

        const added = savedList.includes(FEATURED_SERIES_ID);

        button.textContent = added
            ? "✓ My List"
            : "＋ My List";
    }

    updateButton();

    button.addEventListener("click", () => {

        if (savedList.includes(FEATURED_SERIES_ID)) {

            savedList = savedList.filter(
                id => id !== FEATURED_SERIES_ID
            );

        } else {

            savedList.push(FEATURED_SERIES_ID);
        }

        localStorage.setItem(
            "paperflix_my_list",
            JSON.stringify(savedList)
        );

        updateButton();
    });
}


// =========================================
// 15. SEARCH
// =========================================

function setupSearch() {

    const button = document.querySelector(".icon-button");

    if (!button) return;

    button.addEventListener("click", () => {

        const query = prompt(
            "What research story are you looking for?"
        );

        if (!query) return;

        const normalizedQuery = query.trim().toLowerCase();

        if (!normalizedQuery) return;

        const cards = document.querySelectorAll(
            ".episode-card, .series-card"
        );

        cards.forEach(card => {

            card.hidden = !card.textContent
                .toLowerCase()
                .includes(normalizedQuery);

        });

        const visibleSeriesCards = Array.from(
            document.querySelectorAll(".series-card")
        ).filter(card => !card.hidden);

        const visibleEpisodeCards = Array.from(
            document.querySelectorAll(".episode-card")
        ).filter(card => !card.hidden);

        if (visibleSeriesCards.length) {

            document.getElementById("series")?.scrollIntoView({
                behavior: "smooth",
                block: "start"
            });

        } else if (visibleEpisodeCards.length) {

            const episodeSection = document.getElementById("episodes");

            if (episodeSection) {
                episodeSection.hidden = false;

                episodeSection.scrollIntoView({
                    behavior: "smooth",
                    block: "start"
                });
            }

        } else {

            alert("No matching research series or episodes found.");
        }
    });
}


// =========================================
// 16. INTERACTIVE RESEARCH AREAS
// =========================================

function setupResearchAreas() {

    const areas = document.querySelectorAll(
        ".research-area-card[data-series-id]"
    );

    areas.forEach(area => {

        area.setAttribute("role", "button");
        area.setAttribute("tabindex", "0");

        const activateArea = () => {

            const seriesId = area.dataset.seriesId;

            // Find the matching series card.
            const targetCard = Array.from(
                document.querySelectorAll("#series-list .series-card")
            ).find(card => card.dataset.seriesId === seriesId);

            if (!targetCard) {
                console.warn(
                    `No catalogue card found for research area: ${seriesId}`
                );
                return;
            }

            // Clear previous highlights.
            document.querySelectorAll(
                ".research-area-card.is-active"
            ).forEach(card => {
                card.classList.remove("is-active");
            });

            document.querySelectorAll(
                ".series-card.is-highlighted"
            ).forEach(card => {
                card.classList.remove("is-highlighted");
            });

            // Highlight the selected research area.
            area.classList.add("is-active");
            targetCard.classList.add("is-highlighted");

            // Scroll to its matching series card.
            targetCard.scrollIntoView({
                behavior: "smooth",
                block: "center",
                inline: "center"
            });

            // Remove the temporary series highlight.
            setTimeout(() => {
                targetCard.classList.remove("is-highlighted");
            }, 2500);
        };

        area.addEventListener("click", activateArea);

        // Keyboard accessibility.
        area.addEventListener("keydown", event => {

            if (event.key === "Enter" || event.key === " ") {

                event.preventDefault();
                activateArea();
            }
        });
    });
}



// =========================================
// 16. START SERIES BUTTON
// =========================================

function setupStartButton() {

    const button = document.getElementById("start-series");

    if (!button) return;

    button.addEventListener("click", () => {
        openSeries(FEATURED_SERIES_ID);
    });
}


// =========================================
// 17. APPLICATION STARTUP
// =========================================

async function initializePaperFlix() {

    try {

        await loadSeries();
        setupResearchAreas();

        // Episodes load only after a visitor selects a published series.
        await refreshContinue();

        setupMyList();

        setupSearch();

        setupStartButton();

        console.log("PaperFlix frontend initialized!");

    } catch (error) {

        console.error(
            "PaperFlix initialization failed:",
            error
        );
    }
}


document.addEventListener(
    "DOMContentLoaded",
    initializePaperFlix
);
