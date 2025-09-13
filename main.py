import streamlit as st 
st.title('나의 첫 웹앱!')
st.write('이걸 내가 만들었다고?')
import React, { useState } from "react";
import { motion } from "framer-motion";

// MBTI Study Buddy
// Single-file React component. TailwindCSS required in the host project.
// Drop this component into your Streamret Cloud React app (or any React + Tailwind project).

const MBTIS = [
  "INTJ","INTP","ENTJ","ENTP",
  "INFJ","INFP","ENFJ","ENFP",
  "ISTJ","ISFJ","ESTJ","ESFJ",
  "ISTP","ISFP","ESTP","ESFP"
];

const RECOMMENDATIONS = {
  INTJ: {
    title: "Structure + Deep Dives",
    text: `Make a clear study roadmap. Focus on concept maps and theory-first learning. Schedule deep, distraction-free sessions and summarize each session in bullet points.`,
    emoji: "🧭📚🧠",
    tips: [
      "Plan long-term goals & milestones",
      "Use spaced repetition for core facts",
      "Practice with challenging problems"
    ]
  },
  INTP: {
    title: "Experiment & Play",
    text: `Tinker with ideas, build small experiments, and ask "what if" questions. Alternate focused bursts with playful exploration.`,
    emoji: "🧪🤔✨",
    tips: ["Turn theory into mini-projects","Teach ideas to yourself out loud","Switch subjects to keep curiosity alive"]
  },
  ENTJ: {
    title: "Goals & Efficiency",
    text: `Set ambitious milestones and optimize your study routine. Lead study groups and use time-boxing to crush tasks.`,
    emoji: "🚀🗂️💪",
    tips: ["Assign clear objectives each session","Use Pomodoro + review metrics","Practice timed mock tests"]
  },
  ENTP: {
    title: "Debate & Brainstorm",
    text: `Discuss, argue, and play devil's advocate. Use debates and flash challenges to keep energy high.`,
    emoji: "⚡🗣️🎲",
    tips: ["Make quick idea-buckets","Challenge assumptions","Pair with a study rival"]
  },
  INFJ: {
    title: "Meaningful & Reflective",
    text: `Relate material to personal values. Use storytelling, handwritten summaries, and reflection breaks to internalize learning.`,
    emoji: "🌱📖🕯️",
    tips: ["Create personal case studies","Use quiet review sessions","Connect topics to real-life stories"]
  },
  INFP: {
    title: "Creative & Gentle",
    text: `Learn through metaphors, visuals, and expressive notes. Allow flexible schedules and reward creativity in projects.`,
    emoji: "🎨🌈✍️",
    tips: ["Turn notes into doodles or mind maps","Study in cozy, inspiring spots","Break work into sweet micro-tasks"]
  },
  ENFJ: {
    title: "Group & Purpose",
    text: `Teach others, lead group reviews, and tie study goals to people-focused outcomes. Use feedback loops to improve.`,
    emoji: "🤝📣🌟",
    tips: ["Host mini peer-teaching sessions","Create accountability buddies","Make study goals people-centered"]
  },
  ENFP: {
    title: "Flexible & Passion-led",
    text: `Follow curiosity and vary methods: podcasts, projects, and group brainstorms. Keep tasks playful and purpose-driven.`,
    emoji: "🔥🎧🎉",
    tips: ["Mix media: video, audio, notes","Plan flexible study sprints","Celebrate small wins loudly"]
  },
  ISTJ: {
    title: "Routine & Detail",
    text: `Create a steady routine, detailed checklists, and systematic reviews. Prioritize reliable practice and repetition.`,
    emoji: "🗃️✅⏳",
    tips: ["Use checklists and logs","Daily small reviews","Practice past papers methodically"]
  },
  ISFJ: {
    title: "Supportive & Reliable",
    text: `Study with gentle structure and steady pacing. Use color-coded notes and focus on practical application.`,
    emoji: "🧷📝🫶",
    tips: ["Color-code notes for clarity","Study in familiar spaces","Combine review with gentle rewards"]
  },
  ESTJ: {
    title: "Plan & Execute",
    text: `Set clear schedules, delegate when possible, and track progress. Emphasize disciplined practice and mock exams.`,
    emoji: "📋🏁🔨",
    tips: ["Time-block heavy tasks","Set measurable KPIs","Simulate exam conditions"]
  },
  ESFJ: {
    title: "Social & Structured",
    text: `Study with peers, use cooperative learning, and maintain a pleasant routine. Balance social support with focused review.`,
    emoji: "🌼👥🎀",
    tips: ["Study with trusted friends","Use study playlists","Teach what you learned to someone"]
  },
  ISTP: {
    title: "Hands-on & Tactical",
    text: `Learn by doing—projects, labs, and real-world practice. Keep sessions short and pragmatic.`,
    emoji: "🔧🏍️🧩",
    tips: ["Build or prototype ideas","Practice problem-solving under constraints","Use short focused sessions"]
  },
  ISFP: {
    title: "Sensory & Present",
    text: `Make learning sensory and pleasant with ambient setups, visuals, and short creative projects. Allow for spontaneity.`,
    emoji: "🍃🎶📸",
    tips: ["Study with calming sounds","Use visual note-taking","Take creative mini-breaks"]
  },
  ESTP: {
    title: "Action & Challenge",
    text: `Use fast-paced practice, competitions, and high-energy sprints. Turn study into a game with immediate feedback.`,
    emoji: "🏎️🎯🔥",
    tips: ["Compete in timed quizzes","Use flash challenges","Switch topics to maintain adrenaline"]
  },
  ESFP: {
    title: "Playful & Engaged",
    text: `Keep sessions lively—study parties, songs, and performance-based reviews. Use rewards and social fun.`,
    emoji: "🎉🎤🥳",
    tips: ["Host study parties","Create songs/mnemonics","Reward yourself after sessions"]
  }
};

function FloatingEmojis() {
  // Decorative floating emojis using absolute positioned elements and CSS animations
  return (
    <div aria-hidden className="pointer-events-none absolute inset-0 overflow-hidden">
      {['✨','📚','🎧','🧠','🎲','🚀','💡','🔥'].map((e, i) => (
        <div
          key={i}
          className={`absolute text-2xl md:text-3xl animate-float${i % 3 + 1}`}
          style={{
            left: `${(i * 13) % 100}%`,
            top: `${(i * 11) % 80}%`,
            opacity: 0.85
          }}
        >
          {e}
        </div>
      ))}
    </div>
  );
}

export default function MBTIStudyBuddy() {
  const [mbti, setMbti] = useState('INTJ');
  const info = RECOMMENDATIONS[mbti];

  return (
    <div className="relative min-h-screen bg-gradient-to-br from-indigo-50 via-white to-pink-50 p-6 md:p-12 font-sans">
      <FloatingEmojis />

      <div className="max-w-4xl mx-auto backdrop-blur-sm bg-white/60 dark:bg-gray-900/40 rounded-2xl shadow-xl p-6 md:p-10 border border-white/40">
        <header className="flex items-center justify-between">
          <div>
            <h1 className="text-2xl md:text-4xl font-extrabold tracking-tight">MBTI Study Buddy <span className="text-indigo-600">✨</span></h1>
            <p className="mt-1 text-sm md:text-base text-gray-700">Choose your MBTI and get a fun, emoji-packed study plan with playful effects.</p>
          </div>

          <motion.div whileHover={{ scale: 1.05 }} whileTap={{ scale: 0.95 }} className="text-center">
            <div className="text-xs text-gray-500">Powered by</div>
            <div className="text-lg font-semibold">Streamret Cloud</div>
          </motion.div>
        </header>

        <main className="mt-6 md:mt-8 grid grid-cols-1 md:grid-cols-3 gap-6">
          <section className="md:col-span-1">
            <label className="block text-sm font-medium text-gray-700 mb-2">Pick MBTI</label>
            <select
              value={mbti}
              onChange={(e) => setMbti(e.target.value)}
              className="w-full rounded-lg p-3 border focus:ring-2 focus:ring-indigo-300 shadow-sm"
              aria-label="Select MBTI type"
            >
              {MBTIS.map(t => (
                <option key={t} value={t}>{t}</option>
              ))}
            </select>

            <div className="mt-4 text-sm text-gray-600">
              <strong className="block">Quick tips</strong>
              <ul className="mt-2 space-y-2">
                {info.tips.map((tip, i) => (
                  <li key={i} className="flex items-start gap-2">
                    <motion.span initial={{ x: -6, opacity: 0 }} animate={{ x: 0, opacity: 1 }} transition={{ delay: i * 0.08 }}>{'👉'}</motion.span>
                    <span>{tip}</span>
                  </li>
                ))}
              </ul>
            </div>

            <div className="mt-6">
              <button
                onClick={() => {
                  // simple fun confetti effect by toggling a class — users can wire a library later
                  const el = document.createElement('div');
                  el.className = 'fixed inset-0 z-50 flex items-center justify-center pointer-events-none';
                  el.innerHTML = `<div class="animate-confetti text-4xl">${info.emoji}</div>`;
                  document.body.appendChild(el);
                  setTimeout(() => document.body.removeChild(el), 1400);
                }}
                className="mt-1 inline-flex items-center gap-3 px-4 py-2 rounded-md bg-indigo-600 text-white font-semibold shadow hover:bg-indigo-700 focus:outline-none"
              >
                Celebrate this plan {info.emoji}
              </button>
            </div>
          </section>

          <section className="md:col-span-2">
            <motion.article
              key={mbti}
              initial={{ opacity: 0, y: 12 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ type: 'spring', stiffness: 120 }}
              className="rounded-xl p-6 md:p-8 bg-gradient-to-r from-white to-indigo-50 border border-indigo-100 shadow-lg"
            >
              <div className="flex items-center justify-between">
                <div>
                  <h2 className="text-xl md:text-3xl font-bold">{mbti} — {info.title} <span className="text-2xl ml-2">{info.emoji}</span></h2>
                  <p className="mt-2 text-gray-700 md:text-lg">{info.text}</p>
                </div>

                <motion.div whileHover={{ rotate: 12 }} className="text-5xl">
                  {info.emoji.split('').slice(0,3).join('')}
                </motion.div>
              </div>

              <hr className="my-4 border-dashed" />

              <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                <div className="p-3 rounded-lg bg-white/60 border">
                  <h3 className="font-semibold">Routine</h3>
                  <p className="text-sm mt-1">Set a realistic schedule — short wins beat long soggy sessions.</p>
                </div>
                <div className="p-3 rounded-lg bg-white/60 border">
                  <h3 className="font-semibold">Technique</h3>
                  <p className="text-sm mt-1">Pick 1–2 high-impact methods (e.g., flashcards, practice problems).</p>
                </div>
                <div className="p-3 rounded-lg bg-white/60 border">
                  <h3 className="font-semibold">Reward</h3>
                  <p className="text-sm mt-1">Celebrate every milestone — tiny confetti works wonders.</p>
                </div>
              </div>

              <div className="mt-6 text-sm text-gray-600">Want this as a printable checklist? Click <button className="underline text-indigo-700" onClick={() => window.print()}>Print</button>.</div>
            </motion.article>
          </section>
        </main>

        <footer className="mt-6 text-xs text-gray-500 text-center">Made with ❤️ — tweak the colors, emojis, or tips to match your vibe!</footer>
      </div>

      {/* Tailwind custom animations */}
      <style>{`
        @keyframes float1 { 0% { transform: translateY(0) } 50% { transform: translateY(-12px) } 100% { transform: translateY(0) } }
        @keyframes float2 { 0% { transform: translateY(0) } 50% { transform: translateY(-18px) } 100% { transform: translateY(0) } }
        @keyframes float3 { 0% { transform: translateY(0) } 50% { transform: translateY(-8px) } 100% { transform: translateY(0) } }
        .animate-float1 { animation: float1 6s ease-in-out infinite; }
        .animate-float2 { animation: float2 7s ease-in-out infinite; }
        .animate-float3 { animation: float3 5s ease-in-out infinite; }

        @keyframes confetti { 0% { transform: translateY(-10px) scale(0.9); opacity: 0 } 20% { opacity: 1 } 100% { transform: translateY(200px) scale(1.1); opacity: 0 } }
        .animate-confetti { animation: confetti 1.4s ease-out forwards; }

        /* small responsive tweaks */
        @media (max-width: 640px) {
          .animate-confetti { font-size: 2.2rem }
        }
      `}</style>
    </div>
  );
}
