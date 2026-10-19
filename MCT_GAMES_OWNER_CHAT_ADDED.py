from flask import Flask, render_template_string

app = Flask(__name__)

HTML = r"""
<!doctype html>
<html lang="fa" dir="rtl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no">
<meta name="theme-color" content="#070b16">
<meta name="description" content="MCT GAMES؛ دنیای بازی‌های رایگان و سرگرم‌کننده">
<title>MCT GAMES | دنیای بازی</title>
<style>
:root{--bg:#070b16;--panel:#111a2d;--panel2:#0d1424;--blue:#397bff;--cyan:#52e7ff;--text:#f4f7ff;--muted:#a0aec7;--line:#293956;--card:#131e33}
*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:radial-gradient(ellipse at 10% 0%,#17244a 0,transparent 38%),var(--bg);color:var(--text);font-family:Tahoma,Arial,sans-serif;transition:background .2s,color .2s}
body.light{--bg:#eef4ff;--panel:#fff;--panel2:#f4f7ff;--text:#15213a;--muted:#5c6a83;--line:#cbd7eb;--card:#fff;background:radial-gradient(ellipse at 10% 0%,#dce9ff 0,transparent 42%),var(--bg)}
body.menu-open{overflow:hidden}button,input{font:inherit}button{cursor:pointer}
header{position:sticky;top:0;z-index:20;background:color-mix(in srgb,var(--bg) 92%,transparent);backdrop-filter:blur(18px);border-bottom:1px solid var(--line)}
.nav{max-width:1180px;margin:auto;padding:12px 16px;display:flex;justify-content:space-between;align-items:center;gap:10px}
.logo{display:flex;align-items:center;gap:10px;font-size:22px;font-weight:1000}.logo-mark{width:42px;height:42px;display:grid;place-items:center;border-radius:13px;background:linear-gradient(135deg,#347aff,#8a51ff)}.logo span{color:var(--cyan)}
.nav-actions{display:flex;align-items:center;gap:8px}
.icon-button,.menu-button{width:44px;height:44px;border:1px solid #354966;background:var(--panel);color:var(--text);border-radius:13px;display:grid;place-items:center;font-size:21px}
.menu-button{display:flex;flex-direction:column;justify-content:center;gap:5px}.menu-button span{width:22px;height:2px;border-radius:5px;background:var(--cyan);transition:.2s}.menu-button.active span:first-child{transform:translateY(7px) rotate(45deg)}.menu-button.active span:nth-child(2){opacity:0}.menu-button.active span:last-child{transform:translateY(-7px) rotate(-45deg)}
.menu-overlay{position:fixed;inset:0;z-index:29;background:#0009;opacity:0;visibility:hidden;transition:.25s}.menu-overlay.show{opacity:1;visibility:visible}
.drawer{position:fixed;top:0;right:0;bottom:0;width:min(310px,85vw);z-index:30;padding:22px 18px;background:linear-gradient(160deg,#142440,#080e1c 80%);border-left:1px solid #354966;box-shadow:-15px 0 50px #0005;transform:translateX(105%);transition:transform .28s;overflow-y:auto;color:#eef4ff}.drawer.open{transform:translateX(0)}.drawer-head{display:flex;align-items:center;justify-content:space-between;padding-bottom:20px;border-bottom:1px solid #293956;margin-bottom:20px}.drawer-title{font-weight:bold;font-size:20px}.drawer-title span{color:var(--cyan)}.drawer-close{width:35px;height:35px;border:1px solid #354966;border-radius:10px;background:#172640;color:white;font-size:21px}.drawer-label{color:#8195b7;font-size:12px;margin:0 8px 12px}.drawer-link{width:100%;display:flex;align-items:center;gap:12px;text-align:right;border:1px solid transparent;border-radius:13px;background:transparent;color:#eaf1ff;padding:12px;margin:5px 0;font-size:14px}.drawer-link:hover{background:#1b2d4c;border-color:#35527c}.menu-icon{width:36px;height:36px;display:grid;place-items:center;border-radius:10px;background:#20375c;font-size:18px}.drawer-note{margin-top:25px;padding:15px;border:1px solid #2b4266;border-radius:14px;background:#101c30;color:#a0aec7;font-size:12px;line-height:2}
main{max-width:1180px;margin:auto;padding:22px 18px 55px}.hero{min-height:340px;padding:34px;border:1px solid #304875;border-radius:27px;overflow:hidden;position:relative;background:linear-gradient(135deg,#1a3972,#29194d,#081326);color:#f4f7ff}.hero:after{content:"🎮";position:absolute;left:5%;top:12%;font-size:clamp(100px,22vw,220px);opacity:.18}.hero-content{position:relative;z-index:2;max-width:620px}.eyebrow{display:inline-block;border:1px solid #48628c;background:#0b1428dd;color:#aeefff;padding:9px 13px;border-radius:30px;font-size:13px}.hero h1{font-size:clamp(34px,6vw,59px);line-height:1.3;margin:18px 0 12px}.hero h1 span{color:var(--cyan)}.hero p{color:#d0d9ec;line-height:2;font-size:15px}.primary{border:0;border-radius:13px;padding:13px 20px;background:linear-gradient(110deg,#347cff,#6857ff);color:white;font-weight:bold}.hero-stats{display:flex;gap:20px;flex-wrap:wrap;margin-top:24px;color:#c4d2e9;font-size:12px}.hero-stats b{display:block;color:white;font-size:15px;margin-bottom:5px}
.section-head{display:flex;justify-content:space-between;align-items:center;gap:14px;margin:32px 0 17px}.section-head h2{font-size:23px;margin:0}.section-head p{color:var(--muted);font-size:13px}.search{width:100%;max-width:330px;padding:13px 15px;border-radius:13px;border:1px solid var(--line);background:var(--panel);color:var(--text)}
.filters{display:flex;gap:9px;overflow-x:auto;padding:2px 0 15px}.pill{border:1px solid #354966;background:var(--panel);color:var(--text);border-radius:30px;padding:10px 14px;white-space:nowrap}.filters .active{background:linear-gradient(110deg,#347cff,#6857ff);color:#fff}
.grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:17px}.card{background:linear-gradient(145deg,var(--card),var(--panel2));border:1px solid var(--line);border-radius:20px;overflow:hidden;min-width:0;transition:.25s}.card:hover{transform:translateY(-4px);border-color:#648fff;box-shadow:0 16px 35px #0003}.cover{height:190px;position:relative;overflow:hidden;background:linear-gradient(135deg,#172b50,#382766,#071426)}.cover img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;display:block;z-index:1}.cover img.failed{display:none}.cover-fallback{position:absolute;inset:0;display:grid;place-items:center;font-size:76px;background:radial-gradient(circle at 50% 40%,#263d70,#0b1426 72%);z-index:0}.cover:before{content:"";position:absolute;inset:0;z-index:2;background:linear-gradient(0deg,#080d1bf5 0%,transparent 90%);pointer-events:none}.cover-label{position:absolute;right:13px;left:13px;bottom:13px;display:flex;justify-content:space-between;align-items:center;gap:8px;z-index:3;color:white}.cover-label strong{font-size:16px}.tag{padding:6px 9px;border:1px solid #ffffff40;border-radius:20px;background:#10182bd9;font-size:11px;white-space:nowrap}.card-body{padding:15px}.card h3{margin:0 0 8px;font-size:17px}.card p{min-height:45px;margin:0;color:var(--muted);font-size:13px;line-height:1.9}.card-foot{display:flex;justify-content:space-between;align-items:center;gap:8px;margin-top:15px}.best{font-size:12px;color:#dcae32}.play{border:0;border-radius:10px;padding:10px 14px;background:linear-gradient(110deg,#2874ed,#6457f5);color:white;font-weight:bold}.empty{display:none;padding:30px;text-align:center;color:var(--muted);border:1px dashed #344563;border-radius:15px}
.features{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px;margin-top:28px}.feature{display:flex;align-items:flex-start;gap:12px;padding:17px;background:var(--panel2);border:1px solid var(--line);border-radius:16px}.feature-icon{flex:0 0 40px;height:40px;display:grid;place-items:center;border-radius:12px;background:#1c2c4b;font-size:20px}.feature b{display:block;margin:2px 0 6px}.feature small{color:var(--muted);line-height:1.8}
#gameView,#infoView{display:none}.game-panel{margin-top:20px;padding:20px;text-align:center;border:1px solid var(--line);border-radius:22px;background:linear-gradient(145deg,var(--panel),var(--panel2));overflow:hidden}.game-top{display:flex;justify-content:space-between;align-items:center;gap:9px}.game-top h2{font-size:20px}.stage{min-height:250px;max-width:700px;margin:20px auto;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:12px}.stage canvas{display:block;max-width:100%;height:auto;border:1px solid #273b5e;border-radius:12px;background:#080e1b;touch-action:none}.game-button{border:1px solid #3b5680;background:#182945;color:white;padding:11px 16px;border-radius:11px}.score-strip{display:flex;justify-content:center;gap:10px;flex-wrap:wrap;margin-top:15px}.score-chip{padding:10px 15px;background:var(--panel2);border:1px solid var(--line);border-radius:12px;color:var(--muted);font-size:13px}.score-chip b{color:var(--text)}
.board{display:grid;grid-template-columns:repeat(3,minmax(70px,100px));gap:8px}.cell{height:85px;border-radius:12px;background:#192844;border:1px solid #304768;color:#52e7ff;font-size:35px}.memory{display:grid;grid-template-columns:repeat(4,minmax(50px,72px));gap:8px}.mem{height:65px;font-size:24px;border-radius:10px;border:1px solid #36517c;background:#192844;color:white}.mem.open{background:#2c4d82}
.race-hud{display:flex;justify-content:center;gap:8px;flex-wrap:wrap;margin:4px auto 10px}.race-hud span{padding:8px 10px;background:#101d31;border:1px solid #2d496d;border-radius:10px;color:#dceaff;font-size:12px}.race-hud b{color:#59efff}.race-controls{display:flex;gap:10px;justify-content:center;flex-wrap:wrap;margin:10px auto}.nitro-button{border-color:#8c55ff!important;background:linear-gradient(110deg,#763dff,#d047ff)!important}.joy-wrap{display:flex;flex-direction:column;align-items:center;gap:8px;touch-action:none;user-select:none}.joystick{width:118px;height:118px;border-radius:50%;border:2px solid #45618a;background:radial-gradient(circle,#203b60,#101a2e);position:relative;touch-action:none;box-shadow:0 0 24px #46ddff20}.joy-knob{position:absolute;width:48px;height:48px;left:33px;top:33px;border-radius:50%;background:linear-gradient(135deg,#53f1d1,#3987ff);border:2px solid #b8fbff;box-shadow:0 0 16px #52e7ff88;pointer-events:none}.joy-caption{font-size:12px;color:var(--muted)}.rotate-mode .game-panel{border-color:#52e7ff}.rotate-mode .stage{max-width:none}.rotate-hint{font-size:12px;color:var(--muted)}
.info-card{background:linear-gradient(145deg,var(--card),var(--panel2));border:1px solid var(--line);border-radius:22px;padding:25px;margin-top:20px}.info-card h1{margin:0 0 18px;font-size:27px;color:var(--cyan)}.info-card h2{font-size:19px}.info-card p,.info-card li{color:var(--muted);font-size:14px;line-height:2.2}.info-icon{width:65px;height:65px;display:grid;place-items:center;background:#1b3153;border:1px solid #365783;border-radius:18px;font-size:30px;margin-bottom:17px}.info-highlight{margin-top:15px;padding:15px;border:1px solid var(--line);background:var(--panel2);border-radius:13px;line-height:2}.contact-id{display:inline-block;direction:ltr;unicode-bidi:isolate;padding:10px 14px;background:#142746;border:1px solid #3a5a87;border-radius:10px;color:#65e7ff;font-weight:bold;margin:8px 0}
footer{text-align:center;color:var(--muted);padding:25px 10px;border-top:1px solid var(--line);font-size:13px;line-height:2}footer strong{color:var(--text)}
@media(max-width:800px){.grid{grid-template-columns:repeat(2,minmax(0,1fr))}.features{grid-template-columns:1fr}.hero{padding:28px 22px}}
@media(max-width:480px){main{padding:16px 12px 40px}.grid{grid-template-columns:1fr}.cover{height:190px}.section-head{align-items:stretch;flex-direction:column}.search{max-width:none}.logo{font-size:19px}.game-panel{padding:12px}.game-top h2{font-size:14px}.game-top .pill{padding:8px 9px;font-size:11px}.hero{min-height:310px;padding:24px 18px}.hero h1{font-size:35px}.nav{padding:10px 12px}.info-card{padding:18px}.info-card h1{font-size:23px}}

/* MCT GAMES — visual overhaul */
:root{--electric:#65f4ff;--violet:#9d67ff;--pink:#ff5e9c;--gold:#ffd36a}
body{background-image:radial-gradient(ellipse at 10% -10%,#213d77 0,transparent 42%),radial-gradient(ellipse at 95% 22%,#28134b 0,transparent 35%),linear-gradient(180deg,#070b16,#090f20 60%,#070b16)}
header{background:rgba(7,11,22,.78);border-bottom-color:#34486c;box-shadow:0 8px 32px #0002}
.logo-mark{position:relative;overflow:hidden;box-shadow:0 0 26px #4b7fff55;animation:logoPulse 4s ease-in-out infinite}
.logo-mark:after{content:"";position:absolute;inset:-80% -35%;background:linear-gradient(90deg,transparent,#ffffff55,transparent);transform:rotate(25deg);animation:shine 5s linear infinite}
.hero{min-height:390px;padding:clamp(28px,5vw,52px);border:1px solid #4769a6;border-radius:30px;background:radial-gradient(circle at 82% 28%,#6c44d955,transparent 26%),radial-gradient(circle at 70% 85%,#13cde733,transparent 30%),linear-gradient(125deg,#122c5a 0%,#251849 56%,#081426 100%);box-shadow:0 22px 70px #0004,inset 0 1px #ffffff12}
.hero:before{content:"";position:absolute;inset:0;background-image:radial-gradient(#b7e9ff 1px,transparent 1.5px);background-size:37px 37px;opacity:.16;mask-image:linear-gradient(90deg,transparent,#000)}
.hero:after{content:"⚡";left:7%;top:14%;font-size:clamp(130px,24vw,250px);opacity:.16;filter:drop-shadow(0 0 28px #52e7ff);animation:floatIcon 5s ease-in-out infinite}
.hero-content{max-width:680px}.eyebrow{box-shadow:0 0 24px #52e7ff16;letter-spacing:.1px}.live-dot{display:inline-block;width:7px;height:7px;margin-left:7px;border-radius:50%;background:#57ffbd;box-shadow:0 0 12px #57ffbd;animation:blink 1.6s infinite}
.hero h1{text-shadow:0 4px 28px #0004;letter-spacing:-1px}.hero h1 span{background:linear-gradient(90deg,#67f6ff,#9dbaff 45%,#d1a5ff);-webkit-background-clip:text;background-clip:text;color:transparent;filter:drop-shadow(0 0 18px #4aeaff25)}
.hero .primary,.primary{position:relative;overflow:hidden;box-shadow:0 9px 26px #4b65ff42;transition:transform .2s,box-shadow .2s}.primary:hover,.play:hover{transform:translateY(-2px);box-shadow:0 12px 30px #4b65ff66}.primary:after,.play:after{content:"";position:absolute;inset:0;transform:translateX(-120%);background:linear-gradient(100deg,transparent,#ffffff36,transparent);transition:transform .65s}.primary:hover:after,.play:hover:after{transform:translateX(120%)}
.hero-stats{gap:12px}.hero-stats>div{padding:11px 14px;border:1px solid #ffffff18;border-radius:13px;background:#08132666;backdrop-filter:blur(8px)}
.section-kicker{color:var(--cyan);font-size:10px;font-weight:900;letter-spacing:2px;margin-bottom:7px}.section-head h2{letter-spacing:-.4px}.search{box-shadow:inset 0 1px #ffffff08;transition:border-color .2s,box-shadow .2s}.search:focus{outline:none;border-color:var(--cyan);box-shadow:0 0 0 3px #52e7ff1d}
.filters .pill{transition:transform .18s,border-color .18s,background .18s}.filters .pill:hover{transform:translateY(-2px);border-color:var(--cyan)}
.grid{gap:20px}.card{position:relative;background:linear-gradient(145deg,#141f36dd,#0b1324);border-color:#2c4266;box-shadow:0 10px 30px #00015;transition:transform .28s,border-color .28s,box-shadow .28s}.card:before{content:"";position:absolute;z-index:4;inset:0;border-radius:inherit;padding:1px;background:linear-gradient(135deg,#63edff55,transparent 35%,#a16bff45);-webkit-mask:linear-gradient(#fff 0 0) content-box,linear-gradient(#fff 0 0);-webkit-mask-composite:xor;mask-composite:exclude;pointer-events:none;opacity:.55}.card:hover{transform:translateY(-7px) scale(1.012);border-color:#70cfff;box-shadow:0 20px 42px #0005,0 0 26px #327dff18}.cover{height:205px;background:linear-gradient(135deg,#172b50,#382766,#071426)}.cover img{transition:transform .65s,filter .65s}.card:hover .cover img{transform:scale(1.08);filter:saturate(1.25)}.cover:before{background:linear-gradient(0deg,#080d1b 0%,#080d1b88 22%,transparent 85%)}.cover-label strong{text-shadow:0 2px 12px #000}.tag{box-shadow:0 4px 15px #0003;backdrop-filter:blur(10px)}.card-body{padding:17px}.card h3{font-size:18px}.card p{min-height:49px}.best{color:var(--gold)}.play{position:relative;overflow:hidden;background:linear-gradient(110deg,#2874ed,#7451ff);box-shadow:0 5px 15px #365eff22;transition:transform .2s,box-shadow .2s}
.features{gap:15px}.feature{border-color:#293d60;background:linear-gradient(135deg,#111e33,#0b1323);transition:transform .2s,border-color .2s}.feature:hover{transform:translateY(-3px);border-color:#4d83b9}.feature-icon{background:linear-gradient(135deg,#213d65,#28224d);box-shadow:inset 0 1px #ffffff12}
.game-panel{position:relative;border-color:#334c73;background:radial-gradient(ellipse at 50% 0%,#20365a55,transparent 48%),linear-gradient(145deg,#101a2d,#090f1d);box-shadow:0 22px 55px #0003}.game-panel:before{content:"";position:absolute;pointer-events:none;inset:0;border-radius:inherit;background:linear-gradient(120deg,#6cefff08,transparent 35%,#a06aff08)}.game-top{position:relative;z-index:1}.game-top h2{color:#dcecff;text-shadow:0 0 20px #52e7ff20}.game-button,.pill{transition:transform .15s,border-color .15s,filter .15s}.game-button:active,.pill:active,.play:active,.primary:active{transform:scale(.97)}.score-chip{background:linear-gradient(135deg,#14233b,#0c1525);border-color:#31496d}.score-chip b{color:var(--electric)}
.stage canvas{box-shadow:0 12px 30px #0004,0 0 22px #52e7ff0b}.joystick{border-color:#5b81b3;box-shadow:0 0 0 7px #4adfff08,0 0 28px #46ddff2a;touch-action:none}.joy-knob{box-shadow:0 0 18px #52e7ff99,inset 0 1px #ffffff80}.battle-fire{transition:transform .12s,filter .12s;box-shadow:0 0 0 7px #ff315a12,0 0 28px #ff315a55}.battle-fire:active{transform:scale(.92);filter:brightness(1.25)}
#battleCanvas{box-shadow:0 0 32px #1a7ca522,inset 0 0 30px #000}
.info-card{box-shadow:0 18px 44px #0002}.info-icon{box-shadow:0 0 28px #347aff18}
.challenge-strip{display:flex;align-items:center;gap:15px;margin-top:22px;padding:18px;border:1px solid #3c5280;border-radius:18px;background:radial-gradient(circle at 0 50%,#6a3eff22,transparent 42%),linear-gradient(100deg,#111d35,#0b1323);box-shadow:0 12px 30px #0002}.challenge-symbol{flex:0 0 48px;height:48px;display:grid;place-items:center;border-radius:15px;background:linear-gradient(135deg,#ffb84c,#ff5d88);font-size:24px;box-shadow:0 0 24px #ff6b6b22}.challenge-strip strong{display:block}.challenge-strip p{margin:5px 0 0;color:var(--muted);font-size:12px;line-height:1.8}.challenge-strip .primary{margin-right:auto;white-space:nowrap}@media(max-width:600px){.challenge-strip{align-items:flex-start;flex-wrap:wrap}.challenge-strip .primary{width:100%;margin-right:0}}
@keyframes logoPulse{0%,100%{box-shadow:0 0 18px #4b7fff44}50%{box-shadow:0 0 30px #52e7ff66}}
@keyframes shine{0%{transform:translateX(-160%) rotate(25deg)}45%,100%{transform:translateX(160%) rotate(25deg)}}
@keyframes floatIcon{0%,100%{transform:translateY(0) rotate(-7deg)}50%{transform:translateY(-12px) rotate(5deg)}}
@keyframes blink{0%,100%{opacity:1}50%{opacity:.35}}
@media(max-width:600px){.hero{min-height:360px;border-radius:23px;padding:25px 18px}.hero:after{left:0;top:10%;font-size:140px}.hero-stats{gap:7px}.hero-stats>div{flex:1 1 42%;padding:9px;font-size:11px}.hero-stats b{font-size:13px}.grid{gap:14px}.cover{height:185px}.card:hover{transform:translateY(-2px)}.section-head h2{font-size:21px}}
@media(prefers-reduced-motion:reduce){*,*:before,*:after{animation-duration:.01ms!important;animation-iteration-count:1!important;scroll-behavior:auto!important;transition-duration:.01ms!important}}

/* Layout safety fixes: keep controls in predictable positions on small screens */
.game-top{min-width:0;gap:10px}
.game-top h2{min-width:0;flex:1;text-align:center;overflow-wrap:anywhere}
.game-top>div{flex:0 0 auto;display:flex;align-items:center;justify-content:flex-end;gap:6px}
.game-top .pill{white-space:nowrap;min-height:40px;display:inline-flex;align-items:center;justify-content:center}
.race-controls{width:100%;max-width:360px;display:grid;grid-template-columns:1fr 1fr 1fr;align-items:stretch;gap:8px}
.race-controls .game-button{min-width:0;padding:11px 7px;white-space:nowrap}
.battle-controls{position:relative;z-index:2}
.shooter-wrap{isolation:isolate}
.challenge-strip{min-width:0}
.challenge-strip>div:nth-child(2){min-width:0;flex:1}
.challenge-strip .primary{flex:0 0 auto}
@media(max-width:600px){
  .game-top{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);align-items:center;gap:10px}
  .game-top h2{grid-column:1/-1;grid-row:1;margin:0;padding:4px 0;font-size:17px!important;line-height:1.5}
  .game-top>button:first-child{grid-column:1;grid-row:2;justify-self:start}
  .game-top>div{grid-column:2;grid-row:2;justify-self:end;max-width:100%;gap:5px}
  .game-top .pill{padding:9px 10px!important;font-size:12px!important;min-height:40px}
  .race-controls{grid-template-columns:1fr 1fr 1fr;gap:6px}
  .race-controls .game-button{font-size:12px;padding:11px 4px}
  .battle-controls{gap:14px}
  .battle-fire{width:76px;height:76px}
  .challenge-strip{gap:10px;padding:14px}
}
@media(max-width:360px){
  .game-top>div .pill{padding:8px 7px!important;font-size:11px!important}
  .game-top>button:first-child{padding:8px 9px!important}
  .race-controls .game-button{font-size:11px}
  .shooter-fire{width:56px;height:56px;right:6px;bottom:48px}
}

.enemy-level-toast{position:relative;z-index:5;width:fit-content;max-width:95%;margin:8px auto;padding:9px 14px;border:1px solid #ff9b61;border-radius:12px;background:linear-gradient(120deg,#3b1932,#14213b);color:#fff0d8;text-align:center;font-weight:bold;box-shadow:0 0 20px #ff547844;animation:levelToast .25s ease-out}@keyframes levelToast{from{transform:translateY(8px);opacity:0}to{transform:translateY(0);opacity:1}}
</style>
<script src="https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.min.js"></script>
<style>
#battleCanvas{display:block;width:100%;height:min(62vh,520px);min-height:300px;border:1px solid #315579;border-radius:16px;background:#07101f;touch-action:none}
.battle-hud{display:flex;gap:8px;justify-content:center;flex-wrap:wrap;margin:10px auto}.battle-hud span{padding:8px 11px;border:1px solid #315579;border-radius:10px;background:#0a172a;color:#dceaff;font-size:12px}.battle-hud b{color:#55f2ff}.battle-controls{display:flex;align-items:center;justify-content:center;gap:22px;flex-wrap:wrap;margin:14px auto}.battle-fire{width:88px;height:88px;border-radius:50%;border:2px solid #ff647f;background:radial-gradient(circle at 35% 30%,#ff6c7f,#a80e3c);color:white;font-weight:bold;font-size:25px;box-shadow:0 0 20px #ff315a55;touch-action:none}.battle-help{font-size:12px;line-height:1.9;color:#b8c9e2;text-align:center}.battle-error{padding:14px;border:1px solid #9b4660;border-radius:12px;color:#ffd5df;background:#321321}

.shooter-wrap{position:relative;width:min(100%,430px);margin:0 auto;touch-action:none;user-select:none;overflow:hidden;border:1px solid #294563;border-radius:18px;background:#030816;box-shadow:0 0 24px #39dfff12}.shooter-wrap canvas{width:100%;height:auto;display:block;touch-action:none}.floating-stick{display:none;position:absolute;z-index:4;width:96px;height:96px;transform:translate(-50%,-50%);border:2px solid #72eaffaa;border-radius:50%;background:radial-gradient(circle,#1b4165bb,#0c1a3199);box-shadow:0 0 0 5px #52e7ff12,0 0 22px #52e7ff33;pointer-events:none;backdrop-filter:blur(3px)}.floating-knob{position:absolute;left:26px;top:26px;width:40px;height:40px;border-radius:50%;border:2px solid #d2ffff;background:linear-gradient(135deg,#69ffe1,#4289ff);box-shadow:0 0 16px #52e7ff99}.shooter-controls{display:flex;align-items:center;justify-content:space-around;gap:14px;flex-wrap:wrap;width:min(100%,430px);margin:14px auto;padding:12px;border:1px solid #2d4668;border-radius:16px;background:linear-gradient(135deg,#0d1a2e,#101329)}.shooter-joystick{position:relative;flex:0 0 92px;width:92px;height:92px;border:2px solid #72eaffaa;border-radius:50%;background:radial-gradient(circle,#1b4165,#0c1a31);box-shadow:0 0 0 5px #52e7ff12,0 0 20px #52e7ff22;touch-action:none;user-select:none}.shooter-joystick:after{content:"🕹️";position:absolute;inset:0;display:grid;place-items:center;font-size:22px;opacity:.28;pointer-events:none}.shooter-joystick-knob{position:absolute;left:24px;top:24px;width:40px;height:40px;border-radius:50%;border:2px solid #d2ffff;background:linear-gradient(135deg,#69ffe1,#4289ff);box-shadow:0 0 16px #52e7ff99;z-index:1;pointer-events:none}.shooter-controls .shooter-tip{flex:1 1 100%;order:3}.shooter-fire{position:relative;z-index:3;flex:0 0 auto;min-width:104px;min-height:62px;padding:9px 15px;border-radius:18px;border:2px solid #ffb0bd;background:radial-gradient(circle at 35% 25%,#ff7892,#9e1644);color:white;font-size:23px;box-shadow:0 0 0 4px #ff527a18,0 0 18px #ff527a44;touch-action:none}.shooter-fire span{display:block;font-size:11px;margin-top:2px}.shooter-tip{flex:1 1 190px;padding:10px 12px;border:1px solid #2d4668;border-radius:12px;background:#0b1425;color:#d4e8ff;font-size:11px;line-height:1.8;text-align:center}.game-over-card{padding:16px 20px;border:1px solid #ff6485;border-radius:16px;background:linear-gradient(140deg,#34142a,#10162a);display:flex;align-items:center;justify-content:center;gap:12px;flex-wrap:wrap;color:#fff;box-shadow:0 0 28px #ff315a1a}.game-over-card span{color:#ffcfda;font-size:13px}
@media(max-width:480px){.shooter-controls{gap:8px}.shooter-fire{min-width:90px;min-height:58px;padding:8px 11px}.shooter-tip{font-size:10px;flex-basis:160px}}
</style>
</head>
<body>
<header><div class="nav">
  <div class="logo"><div class="logo-mark">🎮</div><div>MCT <span>GAMES</span></div></div>
  <div class="nav-actions">
    <button class="icon-button" id="themeButton" onclick="toggleTheme()" aria-label="تغییر حالت روشن و تاریک" title="حالت روشن/تاریک">☀️</button>
    <button class="menu-button" id="menuButton" onclick="toggleMenu()" aria-label="باز کردن منو" aria-expanded="false"><span></span><span></span><span></span></button>
  </div>
</div></header>
<div class="menu-overlay" id="menuOverlay" onclick="closeMenu()"></div>
<aside class="drawer" id="drawer" aria-label="منوی سایت">
  <div class="drawer-head"><div class="drawer-title">MCT <span>GAMES</span></div><button class="drawer-close" onclick="closeMenu()" aria-label="بستن منو">×</button></div>
  <div class="drawer-label">منوی اصلی</div>
  <button class="drawer-link" onclick="goHome()"><span class="menu-icon">🏠</span> صفحه اصلی</button>
  <button class="drawer-link" onclick="showGames()"><span class="menu-icon">🎮</span> بازی‌ها</button>
  <button class="drawer-link" onclick="showInfo('about')"><span class="menu-icon">👨‍💻</span> درباره ما</button>
  <button class="drawer-link" onclick="showInfo('contact')"><span class="menu-icon">📩</span> ارتباط با ما</button>
  <button class="drawer-link" onclick="showOwnerNotice()"><span class="menu-icon">💬</span> گفتگو با مالک</button>
  <button class="drawer-link" onclick="showInfo('guide')"><span class="menu-icon">📖</span> راهنمای سایت</button>
  <div class="drawer-note">🎮 به MCT GAMES خوش آمدی!<br>بازی کن، لذت ببر و رکورد خودت را بهتر کن.</div>
</aside>
<main>
<section id="homeView">
  <div class="hero"><div class="hero-content">
    <div class="eyebrow"><span class="live-dot"></span> فصل جدید بازی‌ها · کاملاً رایگان</div>
    <h1>وارد بازی شو،<br><span>رکوردتو بشکن!</span></h1>
    <p>وارد میدان شو، چالش‌ها را رد کن و رکوردت را بشکن! از بازی فکری تا مسابقهٔ نئونی و نبرد سه‌بعدی؛ همه‌چیز همین‌جاست.</p>
    <button class="primary" onclick="showGames()">کشف بازی‌ها ←</button>
    <div class="hero-stats"><div><b>۶ بازی متفاوت</b>از فکری تا اکشن</div><div><b>رایگان</b>بدون نصب جداگانه</div><div><b>لمسی و سریع</b>مخصوص گوشی</div></div>
  </div></div>
  <div class="section-head" id="games"><div><div class="section-kicker">YOUR NEXT CHALLENGE</div><h2>🎮 کدوم بازی جرئتش رو داری؟</h2><p>یکی رو انتخاب کن؛ فقط حواست باشه رکوردت رو از دست ندی!</p></div><input id="search" class="search" placeholder="🔎 جست‌وجوی بازی..." oninput="filterGames()"></div>
  <div class="filters">
    <button class="pill active" onclick="setCategory('all',this)">همه بازی‌ها</button><button class="pill" onclick="setCategory('arcade',this)">🕹 آرکید</button><button class="pill" onclick="setCategory('brain',this)">🧩 فکری</button><button class="pill" onclick="setCategory('action',this)">🚀 اکشن</button>
  </div>
  <div class="grid" id="gameGrid"></div><div class="empty" id="empty">بازی‌ای پیدا نشد؛ عبارت دیگری جست‌وجو کن.</div><div class="challenge-strip"><div class="challenge-symbol">⚡</div><div><strong>چالش امروزت آماده‌ست؟</strong><p>یک بازی انتخاب کن، امتیازت رو بالا ببر و رکورد شخصی‌ات رو جابه‌جا کن.</p></div><button class="primary" onclick="startGame(games[Math.floor(Math.random()*games.length)].id)">🎲 انتخاب شانسی</button></div>
  <div class="features">
    <div class="feature"><div class="feature-icon">🏆</div><div><b>رکوردهای شخصی</b><small>بهترین امتیاز هر بازی در همین مرورگر ذخیره می‌شود.</small></div></div>
    <div class="feature"><div class="feature-icon">📱</div><div><b>مناسب گوشی</b><small>طراحی واکنش‌گرا و کنترل لمسی برای بازی‌های حرکتی.</small></div></div>
    <div class="feature"><div class="feature-icon">⚡</div><div><b>شروع فوری</b><small>بازی‌ها داخل همین صفحه اجرا می‌شوند.</small></div></div>
  </div>
</section>
<section id="infoView">
  <div id="aboutPage" class="info-page" style="display:none"><div class="info-card"><div class="info-icon">👨‍💻</div><h1>درباره MCT GAMES</h1><p>به MCT GAMES خوش آمدی! این سایت با هدف ایجاد فضایی سرگرم‌کننده، ساده و قابل استفاده در گوشی طراحی شده است.</p><p>سازنده این سایت به برنامه‌نویسی علاقه دارد و در مسیر یادگیری پایتون و ساخت پروژه‌های واقعی است.</p><div class="info-highlight"><strong>🎯 هدف ما</strong><br>ترکیب سرگرمی و برنامه‌نویسی و ساخت تجربه‌ای بهتر برای علاقه‌مندان بازی.</div><button class="primary" onclick="showGames()">🎮 دیدن بازی‌ها</button></div></div>
  <div id="contactPage" class="info-page" style="display:none"><div class="info-card"><div class="info-icon">📩</div><h1>ارتباط با ما</h1><p>اگر پیشنهاد، نظر یا مشکلی درباره سایت داری، می‌توانی از شناسه ارتباطی زیر استفاده کنی.</p><div class="info-highlight"><strong>شناسه ارتباطی:</strong><br><span class="contact-id">mct2026@</span><br><button class="primary" onclick="copyContact()">📋 کپی شناسه</button><p id="copyMessage" aria-live="polite"></p></div><p>از پیشنهادها و نظراتت برای بهتر شدن MCT GAMES استقبال می‌کنیم.</p></div></div>
  <div id="guidePage" class="info-page" style="display:none"><div class="info-card"><div class="info-icon">📖</div><h1>راهنمای سایت</h1><h2>🎮 چطور بازی کنم؟</h2><p>۱. وارد بخش بازی‌ها شو.<br>۲. بازی مورد علاقه‌ات را انتخاب کن.<br>۳. روی «بازی کن» بزن.<br>۴. دستورهای بازی را بخوان و شروع کن.</p><h2>🔎 جست‌وجو و دسته‌بندی</h2><p>از کادر جست‌وجو برای پیدا کردن بازی استفاده کن و بازی‌ها را بر اساس دسته‌های آرکید، فکری و اکشن فیلتر کن.</p><h2>🏆 رکوردها</h2><p>بهترین امتیاز هر بازی در حافظه مرورگر دستگاهت ذخیره می‌شود. پاک‌کردن اطلاعات مرورگر ممکن است رکوردها را حذف کند.</p><h2>📱 کنترل بازی‌ها</h2><p>در بازی مار، جنگنده و بتل آرنا از کنترل لمسی استفاده کن. در ماشین می‌توانی از دکمه‌ها یا کشیدن انگشت روی مسیر استفاده کنی. دکمه چرخش تلاش می‌کند صفحه را افقی کند؛ پشتیبانی به مرورگر و گوشی بستگی دارد.</p><button class="primary" onclick="showGames()">🚀 شروع بازی</button></div></div>
</section>
<section id="gameView"><div class="game-panel" id="gamePanel">
  <div class="game-top"><button class="pill" onclick="goHome()">← بازگشت</button><h2 id="gameTitle">بازی</h2><div style="display:flex;gap:6px"><button class="pill" onclick="toggleRotate()" title="چرخش صفحه">⤾ چرخش</button><button class="pill" onclick="restartGame()">↻ دوباره</button></div></div>
  <div id="stage" class="stage"></div><div class="rotate-hint" id="rotateHint"></div>
  <div class="score-strip"><div class="score-chip">🏆 رکورد: <b id="record">۰</b></div><div class="score-chip">⭐ امتیاز: <b id="score">۰</b></div></div>
</div></section>
</main>
<footer><strong>MCT GAMES</strong> © 2026<br>ساخته‌شده برای عاشقان بازی 🎮</footer>
<script>
const games=[
{id:'snake',name:'مار نئونی',desc:'با جوی‌استیک شناور حرکت کن، غذا جمع کن و بزرگ شو.',emoji:'🐍',cover:'https://images.unsplash.com/photo-1535223289827-42f1e9919769?auto=format&fit=crop&w=900&q=85',cat:'arcade',tag:'آرکید'},
{id:'memory',name:'حافظه اسرارآمیز',desc:'کارت‌های یکسان را پیدا کن و امتیاز بگیر.',emoji:'🧠',cover:'https://images.unsplash.com/photo-1519608487953-e999c86e7455?auto=format&fit=crop&w=900&q=85',cat:'brain',tag:'فکری'},
{id:'tictactoe',name:'نبرد دوز',desc:'با هوش مصنوعی رقابت کن و سه‌تایی بساز.',emoji:'❌',cover:'https://images.unsplash.com/photo-1511512578047-dfb367046420?auto=format&fit=crop&w=900&q=85',cat:'brain',tag:'استراتژی'},
{id:'car',name:'ماشین‌بازی نئونی',desc:'ماشین را بین مسیرها هدایت کن و از ترافیک دوری کن.',emoji:'🏎️',cover:'https://images.unsplash.com/photo-1492144534655-ae79c964c9d7?auto=format&fit=crop&w=900&q=85',cat:'action',tag:'رانندگی'},
{id:'shooter',name:'جنگنده کهکشانی',desc:'با جنگنده دشمن‌ها را هدف بگیر و از برخورد دوری کن.',emoji:'🛸',cover:'https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&w=900&q=85',cat:'action',tag:'فضایی'},
{id:'battle',name:'MCT BATTLE ARENA',desc:'میدان نبرد سه‌بعدی؛ در میدان سه‌بعدی زنده بمان، دشمن‌ها را شکست بده و رکورد بساز.',emoji:'🎯',cover:'https://images.unsplash.com/photo-1542751371-adc38448a05e?auto=format&fit=crop&w=900&q=85',cat:'action',tag:'بتل آرنا'}
];
let category='all',currentGame=null,cleanup=null,score=0,rotateMode=false;
const fa=n=>Number(n).toLocaleString('fa-IR');
function toggleMenu(){const d=document.getElementById('drawer'),o=document.getElementById('menuOverlay'),b=document.getElementById('menuButton'),open=!d.classList.contains('open');d.classList.toggle('open',open);o.classList.toggle('show',open);b.classList.toggle('active',open);b.setAttribute('aria-expanded',String(open));document.body.classList.toggle('menu-open',open)}
function closeMenu(){document.getElementById('drawer').classList.remove('open');document.getElementById('menuOverlay').classList.remove('show');document.getElementById('menuButton').classList.remove('active');document.getElementById('menuButton').setAttribute('aria-expanded','false');document.body.classList.remove('menu-open')}
document.addEventListener('keydown',e=>{if(e.key==='Escape')closeMenu()});
function toggleTheme(){const light=document.body.classList.toggle('light');document.getElementById('themeButton').textContent=light?'🌙':'☀️';document.querySelector('meta[name="theme-color"]').content=light?'#eef4ff':'#070b16';try{localStorage.setItem('mct_theme',light?'light':'dark')}catch(e){}}
try{if(localStorage.getItem('mct_theme')==='light'){document.body.classList.add('light');document.getElementById('themeButton').textContent='🌙'}}catch(e){}
function toggleRotate(){rotateMode=!rotateMode;document.body.classList.toggle('rotate-mode',rotateMode);const hint=document.getElementById('rotateHint');if(rotateMode){hint.textContent='حالت چرخش فعال است؛ اگر گوشی نچرخید، چرخش خودکار گوشی را از پنل تنظیمات روشن کن.';try{if(screen.orientation&&screen.orientation.lock)screen.orientation.lock('landscape').catch(()=>{})}catch(e){}}else{hint.textContent='';try{if(screen.orientation&&screen.orientation.unlock)screen.orientation.unlock()}catch(e){}}}
function best(id){try{return Number(localStorage.getItem('mct_best_'+id)||0)}catch(e){return 0}}
function saveBest(){if(!currentGame||score<=best(currentGame))return;try{localStorage.setItem('mct_best_'+currentGame,String(score))}catch(e){}}
function setScore(n){score=n;document.getElementById('score').textContent=fa(score);saveBest();if(currentGame)document.getElementById('record').textContent=fa(best(currentGame))}
function startBattle(){
 base('battle','🎯 MCT BATTLE ARENA');
 const stage=document.getElementById('stage');
 if(typeof THREE==='undefined'){
  stage.innerHTML='<div class="battle-error">کتابخانه سه‌بعدی بارگذاری نشد. اینترنت گوشی را بررسی کن و صفحه را دوباره باز کن.</div>';
  return;
 }
 stage.innerHTML=`<div class="battle-hud"><span>❤️ سلامتی: <b id="battleHealth">۱۰۰</b></span><span>🎯 دشمنان: <b id="battleEnemies">۰</b></span><span>⭐ امتیاز: <b id="battleScore">۰</b></span></div>
 <div id="battleCanvas"></div><div class="battle-controls"><div class="joy-wrap"><div class="joystick" id="battleJoy" aria-label="جوی‌استیک حرکت"><div class="joy-knob" id="battleKnob"></div></div><div class="joy-caption">جوی‌استیک حرکت</div></div><button class="battle-fire" id="battleFire" aria-label="شلیک">🔥</button></div>
 <p class="battle-help">جوی‌استیک را به چپ، راست، جلو یا عقب بکش. دکمه آتش را نگه دار؛ سیستم به نزدیک‌ترین دشمن نشانه می‌گیرد. مراقب سلامتی‌ات باش!</p>`;
 const host=document.getElementById('battleCanvas');
 let alive=true,raf=0,last=0,elapsed=0,spawnTimer=0,fireTimer=0,health=100,points=0,fireHeld=false;
 let axis={x:0,y:0},keys={},enemies=[],bullets=[],damageFlash=0;
 const scene=new THREE.Scene();scene.background=new THREE.Color(0x07101f);scene.fog=new THREE.Fog(0x07101f,24,75);
 const camera=new THREE.PerspectiveCamera(65,1,.1,120);
 const renderer=new THREE.WebGLRenderer({antialias:true,alpha:false,powerPreference:'low-power'});
 renderer.setPixelRatio(Math.min(window.devicePixelRatio||1,1.5));renderer.shadowMap.enabled=false;
 host.appendChild(renderer.domElement);renderer.domElement.style.width='100%';renderer.domElement.style.height='100%';renderer.domElement.style.display='block';renderer.domElement.style.touchAction='none';
 scene.add(new THREE.HemisphereLight(0xb8e7ff,0x172238,2.0));
 const sun=new THREE.DirectionalLight(0xffffff,2);sun.position.set(8,15,8);scene.add(sun);
 const floor=new THREE.Mesh(new THREE.PlaneGeometry(100,100),new THREE.MeshStandardMaterial({color:0x101f31,roughness:1,metalness:0}));floor.rotation.x=-Math.PI/2;floor.position.y=-.08;scene.add(floor);
 const grid=new THREE.GridHelper(100,50,0x176a86,0x18324b);grid.position.y=-.05;scene.add(grid);
 // مرزهای میدان و موانع تزئینی
 for(let i=0;i<18;i++){
  const a=i*Math.PI*2/18,r=17+(i%3)*1.5;
  const m=new THREE.Mesh(new THREE.BoxGeometry(1.2,1.4,1.2),new THREE.MeshStandardMaterial({color:i%2?0x163e57:0x342451,emissive:i%2?0x06202b:0x170829,roughness:.8}));
  m.position.set(Math.cos(a)*r,.7,Math.sin(a)*r);scene.add(m);
 }
 const player=new THREE.Group();scene.add(player);
 const body=new THREE.Mesh(new THREE.CapsuleGeometry(.48,.85,4,8),new THREE.MeshStandardMaterial({color:0x16bde2,metalness:.25,roughness:.45}));body.position.y=.85;player.add(body);
 const visor=new THREE.Mesh(new THREE.BoxGeometry(.48,.2,.12),new THREE.MeshStandardMaterial({color:0xc5fbff,emissive:0x164a66}));visor.position.set(0,1.25,-.39);player.add(visor);
 const gun=new THREE.Mesh(new THREE.BoxGeometry(.18,.18,.8),new THREE.MeshStandardMaterial({color:0x25354a,metalness:.65,roughness:.3}));gun.position.set(.38,.95,-.42);player.add(gun);
 player.position.set(0,0,5);
 const enemyGeo=new THREE.CapsuleGeometry(.45,.75,3,7);
 function spawnEnemy(){
  const a=Math.random()*Math.PI*2,r=12+Math.random()*7;
  const g=new THREE.Group();
  const mat=new THREE.MeshStandardMaterial({color:0xff416b,emissive:0x4b0719,metalness:.15,roughness:.55});
  const torso=new THREE.Mesh(enemyGeo,mat);torso.position.y=.78;g.add(torso);
  const head=new THREE.Mesh(new THREE.SphereGeometry(.28,8,7),new THREE.MeshStandardMaterial({color:0xffb0bd,emissive:0x321018}));head.position.y=1.55;g.add(head);
  const eye=new THREE.Mesh(new THREE.BoxGeometry(.24,.07,.05),new THREE.MeshBasicMaterial({color:0xfff2b0}));eye.position.set(0,1.58,-.25);g.add(eye);
  g.position.set(Math.cos(a)*r,0,Math.sin(a)*r);scene.add(g);enemies.push({mesh:g,hp:2+Math.floor(elapsed/45),speed:1.0+Math.random()*.45,hit:0});
 }
 function resize(){const w=Math.max(260,host.clientWidth||320),h=Math.max(300,host.clientHeight||380);renderer.setSize(w,h,false);camera.aspect=w/h;camera.updateProjectionMatrix()}
 resize();const resizeObserver=typeof ResizeObserver!=='undefined'?new ResizeObserver(resize):null;if(resizeObserver)resizeObserver.observe(host);window.addEventListener('resize',resize);
 function joystickMove(e){const r=joy.getBoundingClientRect(),dx=e.clientX-(r.left+r.width/2),dy=e.clientY-(r.top+r.height/2),dist=Math.hypot(dx,dy),lim=30,m=Math.min(1,lim/(dist||1));knob.style.left=(33+dx*m)+'px';knob.style.top=(33+dy*m)+'px';axis={x:dx/(dist||1)*Math.min(1,dist/25),y:dy/(dist||1)*Math.min(1,dist/25)}}
 const joy=document.getElementById('battleJoy'),knob=document.getElementById('battleKnob');let dragging=false;
 function joyDown(e){e.preventDefault();dragging=true;joy.setPointerCapture?.(e.pointerId);joystickMove(e)}function joyMove(e){if(dragging)joystickMove(e)}function joyUp(){dragging=false;axis={x:0,y:0};knob.style.left='33px';knob.style.top='33px'}
 joy.addEventListener('pointerdown',joyDown);joy.addEventListener('pointermove',joyMove);joy.addEventListener('pointerup',joyUp);joy.addEventListener('pointercancel',joyUp);
 const fireBtn=document.getElementById('battleFire');function fireDown(e){e.preventDefault();fireHeld=true;fireBtn.setPointerCapture?.(e.pointerId)}function fireUp(){fireHeld=false}
 fireBtn.addEventListener('pointerdown',fireDown);fireBtn.addEventListener('pointerup',fireUp);fireBtn.addEventListener('pointercancel',fireUp);fireBtn.addEventListener('pointerleave',fireUp);
 function keyDown(e){if(['ArrowUp','ArrowDown','ArrowLeft','ArrowRight','w','a','s','d',' '].includes(e.key)){e.preventDefault();keys[e.key]=true;if(e.key===' ')fireHeld=true}}
 function keyUp(e){keys[e.key]=false;if(e.key===' ')fireHeld=false}window.addEventListener('keydown',keyDown);window.addEventListener('keyup',keyUp);
 function makeShot(target){
  const start=new THREE.Vector3(player.position.x,1.1,player.position.z-0.5);
  const end=target?target.mesh.position.clone().add(new THREE.Vector3(0,1,0)):new THREE.Vector3(player.position.x,1,player.position.z-10);
  const dir=end.sub(start).normalize();const mesh=new THREE.Mesh(new THREE.SphereGeometry(.12,7,6),new THREE.MeshBasicMaterial({color:0x61f7ff}));mesh.position.copy(start);scene.add(mesh);bullets.push({mesh,dir,life:1.5});
 }
 function updateHud(){document.getElementById('battleHealth').textContent=fa(Math.max(0,Math.ceil(health)));document.getElementById('battleEnemies').textContent=fa(enemies.length);document.getElementById('battleScore').textContent=fa(points);setScore(points)}
 function endGame(){alive=false;stage.insertAdjacentHTML('beforeend','<h3 style="color:#ffb9c7">💥 ماموریت تمام شد!</h3><p>امتیاز نهایی: '+fa(points)+'</p><button class="primary" onclick="restartGame()">🔄 نبرد دوباره</button>')}
 function frame(t){
  if(!alive)return;if(!last)last=t;const dt=Math.min((t-last)/1000,.04);last=t;elapsed+=dt;spawnTimer+=dt;fireTimer-=dt;damageFlash=Math.max(0,damageFlash-dt);
  let mx=axis.x,my=axis.y;if(keys.ArrowLeft||keys.a)mx=-1;if(keys.ArrowRight||keys.d)mx=1;if(keys.ArrowUp||keys.w)my=-1;if(keys.ArrowDown||keys.s)my=1;
  const len=Math.hypot(mx,my);if(len>1){mx/=len;my/=len}
  player.position.x+=mx*5.4*dt;player.position.z+=my*5.4*dt;player.position.x=Math.max(-15,Math.min(15,player.position.x));player.position.z=Math.max(-15,Math.min(15,player.position.z));
  if(Math.abs(mx)+Math.abs(my)>.08)player.rotation.y=Math.atan2(mx,-my);
  if(spawnTimer>Math.max(.65,1.65-elapsed*.012)&&enemies.length<12){spawnTimer=0;spawnEnemy()}
  if(fireHeld&&fireTimer<=0){let target=null,bestDist=Infinity;for(const e of enemies){const d=e.mesh.position.distanceTo(player.position);if(d<bestDist){bestDist=d;target=e}}makeShot(target);fireTimer=.24}
  for(let i=bullets.length-1;i>=0;i--){const b=bullets[i];b.mesh.position.addScaledVector(b.dir,17*dt);b.life-=dt;let hit=false;for(let j=enemies.length-1;j>=0;j--){const e=enemies[j];if(b.mesh.position.distanceTo(e.mesh.position.clone().add(new THREE.Vector3(0,1,0)))<.8){e.hp--;scene.remove(b.mesh);bullets.splice(i,1);hit=true;if(e.hp<=0){scene.remove(e.mesh);enemies.splice(j,1);points+=10}break}}if(!hit&&b.life<=0){scene.remove(b.mesh);bullets.splice(i,1)}}
  for(let i=enemies.length-1;i>=0;i--){const e=enemies[i],dx=player.position.x-e.mesh.position.x,dz=player.position.z-e.mesh.position.z,d=Math.hypot(dx,dz)||1;e.mesh.position.x+=(dx/d)*e.speed*dt;e.mesh.position.z+=(dz/d)*e.speed*dt;e.mesh.lookAt(player.position.x,1,player.position.z);if(d<1.25){health-=22*dt;if(health<=0){health=0;updateHud();endGame();return}}}
  camera.position.lerp(new THREE.Vector3(player.position.x,5.3,player.position.z+7.8),Math.min(1,dt*4));camera.lookAt(player.position.x,.6,player.position.z-2.2);
  renderer.render(scene,camera);updateHud();raf=requestAnimationFrame(frame);
 }
 updateHud();for(let i=0;i<4;i++)spawnEnemy();raf=requestAnimationFrame(frame);
 cleanup=()=>{alive=false;if(raf)cancelAnimationFrame(raf);if(resizeObserver)resizeObserver.disconnect();window.removeEventListener('resize',resize);window.removeEventListener('keydown',keyDown);window.removeEventListener('keyup',keyUp);joy.removeEventListener('pointerdown',joyDown);joy.removeEventListener('pointermove',joyMove);joy.removeEventListener('pointerup',joyUp);joy.removeEventListener('pointercancel',joyUp);fireBtn.removeEventListener('pointerdown',fireDown);fireBtn.removeEventListener('pointerup',fireUp);fireBtn.removeEventListener('pointercancel',fireUp);fireBtn.removeEventListener('pointerleave',fireUp);enemies.forEach(e=>scene.remove(e.mesh));bullets.forEach(b=>scene.remove(b.mesh));renderer.dispose();if(renderer.domElement.parentNode)renderer.domElement.parentNode.removeChild(renderer.domElement)};
}

function filterGames(){const q=document.getElementById('search').value.trim().toLowerCase();const list=games.filter(g=>(category==='all'||g.cat===category)&&(g.name.toLowerCase().includes(q)||g.desc.toLowerCase().includes(q)||g.tag.toLowerCase().includes(q)));document.getElementById('gameGrid').innerHTML=list.map(g=>`<article class="card"><div class="cover"><div class="cover-fallback">${g.emoji}</div><img src="${g.cover}" alt="${g.name}" loading="lazy" onerror="this.classList.add('failed')"><div class="cover-label"><strong>${g.emoji} ${g.name}</strong><span class="tag">${g.tag}</span></div></div><div class="card-body"><h3>${g.name}</h3><p>${g.desc}</p><div class="card-foot"><span class="best">🏆 ${fa(best(g.id))}</span><button class="play" onclick="startGame('${g.id}')">بازی کن ←</button></div></div></article>`).join('');document.getElementById('empty').style.display=list.length?'none':'block'}
function setCategory(c,b){category=c;document.querySelectorAll('.filters button').forEach(x=>x.classList.remove('active'));b.classList.add('active');filterGames()}
function stopCurrentGame(){if(cleanup){cleanup();cleanup=null}}
function goHome(){closeMenu();stopCurrentGame();document.getElementById('gameView').style.display='none';document.getElementById('infoView').style.display='none';document.getElementById('homeView').style.display='block';filterGames();window.scrollTo({top:0,behavior:'smooth'})}
function showGames(){closeMenu();stopCurrentGame();document.getElementById('gameView').style.display='none';document.getElementById('infoView').style.display='none';document.getElementById('homeView').style.display='block';filterGames();setTimeout(()=>document.getElementById('games').scrollIntoView({behavior:'smooth'}),50)}
function showInfo(page){closeMenu();stopCurrentGame();document.getElementById('homeView').style.display='none';document.getElementById('gameView').style.display='none';document.getElementById('infoView').style.display='block';document.querySelectorAll('.info-page').forEach(p=>p.style.display='none');const s=document.getElementById(page+'Page');if(s)s.style.display='block';window.scrollTo({top:0,behavior:'smooth'})}
function showOwnerNotice(){closeMenu();alert('این بخش هنوز آماده نشده است؛ به‌زودی آماده می‌شود.')}
function copyContact(){const v='mct2026@',m=document.getElementById('copyMessage');if(navigator.clipboard&&window.isSecureContext){navigator.clipboard.writeText(v).then(()=>m.textContent='شناسه کپی شد! ✅').catch(()=>m.textContent='شناسه را انتخاب و کپی کن: '+v)}else m.textContent='شناسه: '+v+' — آن را انتخاب و کپی کن.'}
function base(id,title){stopCurrentGame();currentGame=id;score=0;document.getElementById('homeView').style.display='none';document.getElementById('infoView').style.display='none';document.getElementById('gameView').style.display='block';document.getElementById('gameTitle').textContent=title;document.getElementById('record').textContent=fa(best(id));document.getElementById('score').textContent=fa(0);document.getElementById('stage').innerHTML='';document.getElementById('rotateHint').textContent='';window.scrollTo(0,0)}
function restartGame(){if(currentGame)startGame(currentGame)}
function startGame(id){closeMenu();if(id==='snake')startSnake();if(id==='memory')startMemory();if(id==='tictactoe')startTic();if(id==='car')startCar();if(id==='shooter')startShooter();if(id==='battle')startBattle()}

function startSnake(){
base('snake','🐍 مار نئونی');const stage=document.getElementById('stage');stage.innerHTML=`<canvas id="snakeCanvas" width="320" height="320"></canvas><div class="joy-wrap"><div class="joystick" id="joystick" aria-label="جوی‌استیک شناور"><div class="joy-knob" id="joyKnob"></div></div><div class="joy-caption">انگشتت را داخل دایره بکش تا جهت مار عوض شود</div></div><p>سرعت آرام‌تر شده؛ غذا بخور و به دیوار یا بدنت برخورد نکن.</p>`;
const c=document.getElementById('snakeCanvas'),ctx=c.getContext('2d'),size=16,cell=20;let snake=[{x:7,y:8},{x:6,y:8},{x:5,y:8}],dir={x:1,y:0},next={x:1,y:0},food,dead=false;
function newFood(){do{food={x:Math.floor(Math.random()*size),y:Math.floor(Math.random()*size)}}while(snake.some(p=>p.x===food.x&&p.y===food.y))}
function setDir(x,y){if(x!==-dir.x||y!==-dir.y)next={x,y}}
function key(e){const k={ArrowUp:[0,-1],ArrowDown:[0,1],ArrowLeft:[-1,0],ArrowRight:[1,0],w:[0,-1],s:[0,1],a:[-1,0],d:[1,0]};if(k[e.key]){e.preventDefault();setDir(...k[e.key])}}window.addEventListener('keydown',key);
const joy=document.getElementById('joystick'),knob=document.getElementById('joyKnob');let dragging=false;
function joyMove(e){const r=joy.getBoundingClientRect(),cx=r.left+r.width/2,cy=r.top+r.height/2,dx=e.clientX-cx,dy=e.clientY-cy,dist=Math.hypot(dx,dy),lim=30,m=Math.min(1,lim/(dist||1));knob.style.left=(33+dx*m)+'px';knob.style.top=(33+dy*m)+'px';if(dist>12){if(Math.abs(dx)>Math.abs(dy))setDir(dx>0?1:-1,0);else setDir(0,dy>0?1:-1)}}
function down(e){dragging=true;joy.setPointerCapture?.(e.pointerId);joyMove(e)}function move(e){if(dragging)joyMove(e)}function up(){dragging=false;knob.style.left='33px';knob.style.top='33px'}joy.addEventListener('pointerdown',down);joy.addEventListener('pointermove',move);joy.addEventListener('pointerup',up);joy.addEventListener('pointercancel',up);
function draw(){ctx.fillStyle='#080e1b';ctx.fillRect(0,0,320,320);ctx.strokeStyle='#182944';for(let i=0;i<=size;i++){ctx.beginPath();ctx.moveTo(i*cell,0);ctx.lineTo(i*cell,320);ctx.stroke();ctx.beginPath();ctx.moveTo(0,i*cell);ctx.lineTo(320,i*cell);ctx.stroke()}ctx.fillStyle='#ffca4a';ctx.beginPath();ctx.arc(food.x*cell+10,food.y*cell+10,8,0,Math.PI*2);ctx.fill();snake.forEach((p,i)=>{ctx.fillStyle=i?'#318b9d':'#53f1d1';ctx.shadowBlur=i?0:12;ctx.shadowColor='#53f1d1';ctx.fillRect(p.x*cell+2,p.y*cell+2,16,16)});ctx.shadowBlur=0}
function tick(){if(dead)return;dir=next;const h={x:snake[0].x+dir.x,y:snake[0].y+dir.y};if(h.x<0||h.y<0||h.x>=size||h.y>=size||snake.some(p=>p.x===h.x&&p.y===h.y)){dead=true;clearInterval(timer);stage.insertAdjacentHTML('beforeend','<h3>💥 بازی تمام شد!</h3><button class="primary" onclick="restartGame()">دوباره بازی کن</button>');return}snake.unshift(h);if(h.x===food.x&&h.y===food.y){setScore(score+10);newFood()}else snake.pop();draw()}
newFood();draw();const timer=setInterval(tick,220);cleanup=()=>{clearInterval(timer);window.removeEventListener('keydown',key);joy.removeEventListener('pointerdown',down);joy.removeEventListener('pointermove',move);joy.removeEventListener('pointerup',up);joy.removeEventListener('pointercancel',up)}
}
function startMemory(){base('memory','🧠 حافظه اسرارآمیز');const stage=document.getElementById('stage'),icons=['🐸','🐸','🍕','🍕','🚀','🚀','👻','👻','🎲','🎲','🐼','🐼','⚽','⚽','💎','💎'].sort(()=>Math.random()-.5);stage.innerHTML='<p>دو کارت یکسان را پیدا کن.</p><div class="memory" id="memoryBoard"></div><p id="memoryInfo">حرکت‌ها: ۰</p>';let first=null,lock=false,moves=0,matched=0,timers=[];const board=document.getElementById('memoryBoard');icons.forEach(v=>{const b=document.createElement('button');b.className='mem';b.textContent='?';b.onclick=()=>{if(lock||b.classList.contains('open')||b.dataset.done)return;b.textContent=v;b.classList.add('open');if(!first){first=b;return}moves++;document.getElementById('memoryInfo').textContent='حرکت‌ها: '+fa(moves);if(first.textContent===b.textContent){first.dataset.done='1';b.dataset.done='1';matched+=2;setScore(score+10);first=null;if(matched===icons.length)stage.insertAdjacentHTML('beforeend','<h3>🎉 آفرین! همه جفت‌ها پیدا شدند.</h3>')}else{lock=true;const old=first;timers.push(setTimeout(()=>{old.textContent='?';b.textContent='?';old.classList.remove('open');b.classList.remove('open');first=null;lock=false},650))}};board.appendChild(b)});cleanup=()=>timers.forEach(clearTimeout)}
function startTic(){base('tictactoe','❌ نبرد دوز');const stage=document.getElementById('stage');stage.innerHTML='<p>تو X هستی؛ با کامپیوتر بازی کن.</p><div class="board" id="ticBoard"></div><h3 id="ticMessage">نوبت توست!</h3><button class="game-button" onclick="startTic()">شروع دوباره</button>';let cells=Array(9).fill(''),done=false,aiTimer=null;const board=document.getElementById('ticBoard'),msg=document.getElementById('ticMessage'),wins=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]];function winner(){for(const l of wins)if(cells[l[0]]&&cells[l[0]]===cells[l[1]]&&cells[l[1]]===cells[l[2]])return cells[l[0]];return cells.every(Boolean)?'draw':null}function render(){board.innerHTML='';cells.forEach((v,i)=>{const b=document.createElement('button');b.className='cell';b.textContent=v;b.onclick=()=>play(i);board.appendChild(b)})}function finish(r){done=true;msg.textContent=r==='X'?'🏆 تو بردی!':r==='O'?'🤖 کامپیوتر برد!':'مساوی شد!';if(r==='X')setScore(score+50)}function play(i){if(done||cells[i])return;cells[i]='X';render();let r=winner();if(r){finish(r);return}msg.textContent='کامپیوتر فکر می‌کند...';aiTimer=setTimeout(()=>{if(done)return;const empty=cells.map((v,i)=>v?null:i).filter(v=>v!==null);if(!empty.length){finish('draw');return}let m=empty.find(i=>{let t=cells.slice();t[i]='O';return wins.some(l=>l.every(j=>t[j]==='O'))});if(m===undefined)m=empty.find(i=>{let t=cells.slice();t[i]='X';return wins.some(l=>l.every(j=>t[j]==='X'))});if(m===undefined&&!cells[4])m=4;if(m===undefined)m=empty[Math.floor(Math.random()*empty.length)];cells[m]='O';render();r=winner();if(r)finish(r);else msg.textContent='نوبت توست!'},300)}render();cleanup=()=>clearTimeout(aiTimer)}
function startCar(){
base('car','🏁 توربو ریسینگ');const stage=document.getElementById('stage');
stage.innerHTML='<div class="race-hud"><span>🏆 امتیاز <b id="raceScore">۰</b></span><span>🪙 سکه <b id="raceCoins">۰</b></span><span>⚡ نیترو <b id="raceNitro">آماده</b></span><span>🚦 مرحله <b id="raceLevel">۱</b></span></div><canvas id="carCanvas" width="360" height="520" style="width:min(100%,360px);touch-action:none"></canvas><div class="race-controls"><button class="game-button" id="carLeft" aria-label="حرکت به چپ">⬅️ چپ</button><button class="game-button nitro-button" id="carNitro">⚡ نیترو</button><button class="game-button" id="carRight" aria-label="حرکت به راست">راست ➡️</button></div><p>از ترافیک جاخالی بده، سکه‌های طلایی را جمع کن و نیترو را برای لحظهٔ حساس نگه دار! هرچه بیشتر دوام بیاوری، سرعت و سختی بالاتر می‌رود.</p>';
const c=document.getElementById('carCanvas'),ctx=c.getContext('2d');let lane=1,traffic=[],coins=[],alive=true,last=0,elapsed=0,spawn=0,coinSpawn=0,raf,nitro=0,coinCount=0,downX=null,moveCooldown=0,lastLaneChange=0;
function shift(d){const now=performance.now();if(now-lastLaneChange<115)return;const nextLane=Math.max(0,Math.min(2,lane+d));if(nextLane!==lane){lane=nextLane;lastLaneChange=now;const hud=document.getElementById('raceLevel');if(hud)hud.textContent=fa(1+Math.floor(elapsed/18))}}document.getElementById('carLeft').onclick=()=>shift(-1);document.getElementById('carRight').onclick=()=>shift(1);document.getElementById('carNitro').onclick=()=>{if(nitro<=0)nitro=2.2};
function key(e){if(['ArrowLeft','ArrowRight','a','d',' '].includes(e.key))e.preventDefault();if(e.key==='ArrowLeft'||e.key==='a')shift(-1);if(e.key==='ArrowRight'||e.key==='d')shift(1);if(e.key===' ')nitro=2.2}window.addEventListener('keydown',key);
c.addEventListener('pointerdown',e=>{downX=e.clientX;c.setPointerCapture?.(e.pointerId)});c.addEventListener('pointerup',e=>{if(downX!==null){let dx=e.clientX-downX;if(Math.abs(dx)>18)shift(dx>0?1:-1);downX=null}});c.addEventListener('pointercancel',()=>downX=null);
function laneX(l){return 90+l*90}
function drawCar(cx,cy,color,player=false){ctx.save();ctx.translate(cx,cy);ctx.shadowColor=player?'#46efff':'#ff4c77';ctx.shadowBlur=player?13:5;ctx.fillStyle='#080b12';ctx.fillRect(-23,-20,7,18);ctx.fillRect(16,-20,7,18);ctx.fillRect(-23,10,7,18);ctx.fillRect(16,10,7,18);let g=ctx.createLinearGradient(-18,0,18,0);g.addColorStop(0,color);g.addColorStop(.5,player?'#d7ffff':'#ffd4de');g.addColorStop(1,color);ctx.fillStyle=g;ctx.beginPath();ctx.moveTo(-16,25);ctx.lineTo(-19,-12);ctx.quadraticCurveTo(-17,-26,-8,-28);ctx.lineTo(8,-28);ctx.quadraticCurveTo(17,-26,19,-12);ctx.lineTo(16,25);ctx.closePath();ctx.fill();ctx.shadowBlur=0;ctx.fillStyle='#152b42';ctx.beginPath();ctx.moveTo(-12,-12);ctx.lineTo(-9,-22);ctx.lineTo(9,-22);ctx.lineTo(12,-12);ctx.closePath();ctx.fill();ctx.fillStyle='#aef8ff';ctx.fillRect(-13,15,6,4);ctx.fillRect(7,15,6,4);ctx.fillStyle='#fff2a6';ctx.fillRect(-13,-25,5,3);ctx.fillRect(8,-25,5,3);ctx.restore()}
function frame(t){if(!alive)return;if(!last)last=t;const dt=Math.min((t-last)/1000,.04);last=t;elapsed+=dt;moveCooldown=Math.max(0,moveCooldown-dt);nitro=Math.max(0,nitro-dt);let speed=(185+Math.min(elapsed*5,95))*(nitro>0?1.75:1);spawn+=dt;coinSpawn+=dt;if(spawn>Math.max(.48,.95-elapsed*.006)){spawn=0;let l=Math.floor(Math.random()*3);traffic.push({lane:l,y:-55,color:['#ff4d79','#ffad42','#a78bfa','#72f29b'][Math.floor(Math.random()*4)],speed:.82+Math.random()*.35})}if(coinSpawn>1.15){coinSpawn=0;coins.push({lane:Math.floor(Math.random()*3),y:-20,spin:0})}traffic.forEach(a=>a.y+=speed*a.speed*dt);coins.forEach(a=>{a.y+=speed*dt;a.spin+=dt*7});traffic=traffic.filter(a=>a.y<570);coins=coins.filter(a=>a.y<560);
ctx.fillStyle='#06101b';ctx.fillRect(0,0,360,520);ctx.fillStyle='#0d332d';ctx.fillRect(0,0,45,520);ctx.fillRect(315,0,45,520);
// stylized road with glowing shoulders
ctx.fillStyle='#252d40';ctx.beginPath();ctx.moveTo(75,0);ctx.lineTo(285,0);ctx.lineTo(330,520);ctx.lineTo(30,520);ctx.closePath();ctx.fill();ctx.strokeStyle='#47d9ff';ctx.lineWidth=3;ctx.shadowColor='#47d9ff';ctx.shadowBlur=10;ctx.beginPath();ctx.moveTo(75,0);ctx.lineTo(30,520);ctx.moveTo(285,0);ctx.lineTo(330,520);ctx.stroke();ctx.shadowBlur=0;
ctx.strokeStyle='#d7e5ff';ctx.lineWidth=3;ctx.setLineDash([27,24]);ctx.lineDashOffset=-(elapsed*speed*.65)%51;ctx.beginPath();ctx.moveTo(145,0);ctx.lineTo(115,520);ctx.moveTo(215,0);ctx.lineTo(245,520);ctx.stroke();ctx.setLineDash([]);
// roadside lights
for(let i=0;i<9;i++){let y=(i*75+(elapsed*speed*1.2)%75)%540;ctx.fillStyle='#f9d56e';ctx.fillRect(52,y,4,13);ctx.fillRect(304,y,4,13)}
coins.forEach(a=>{ctx.save();ctx.translate(laneX(a.lane),a.y);ctx.rotate(Math.sin(a.spin)*.2);ctx.fillStyle='#ffcb45';ctx.shadowColor='#ffcb45';ctx.shadowBlur=12;ctx.beginPath();ctx.arc(0,0,11,0,Math.PI*2);ctx.fill();ctx.shadowBlur=0;ctx.fillStyle='#7b4b09';ctx.font='bold 14px Arial';ctx.textAlign='center';ctx.textBaseline='middle';ctx.fillText('$',0,1);ctx.restore();if(a.lane===lane&&Math.abs(a.y-420)<30){a.y=600;coinCount++;setScore(score+25);document.getElementById('raceCoins').textContent=fa(coinCount)}});
traffic.forEach(a=>drawCar(laneX(a.lane),a.y,a.color));drawCar(laneX(lane),420,nitro>0?'#f8a9ff':'#35dfff',true);
if(nitro>0){ctx.strokeStyle='#a9faff';ctx.lineWidth=4;ctx.shadowColor='#5ff7ff';ctx.shadowBlur=15;ctx.beginPath();ctx.moveTo(laneX(lane)-8,448);ctx.lineTo(laneX(lane)-5,480);ctx.moveTo(laneX(lane)+8,448);ctx.lineTo(laneX(lane)+5,480);ctx.stroke();ctx.shadowBlur=0}
for(const a of traffic){if(a.lane===lane&&Math.abs(a.y-420)<43){alive=false;setScore(score+Math.floor(elapsed*4));stage.insertAdjacentHTML('beforeend','<h3>💥 تصادف! مسابقه تموم شد.</h3><button class="primary" onclick="restartGame()">🏁 مسابقه دوباره</button>');return}}
setScore(Math.floor(elapsed*5)+coinCount*25);document.getElementById('raceScore').textContent=fa(score);document.getElementById('raceCoins').textContent=fa(coinCount);document.getElementById('raceNitro').textContent=nitro>0?'فعال ⚡':'آماده';const levelHud=document.getElementById('raceLevel');if(levelHud)levelHud.textContent=fa(1+Math.floor(elapsed/18));raf=requestAnimationFrame(frame)}raf=requestAnimationFrame(frame);cleanup=()=>{alive=false;cancelAnimationFrame(raf);window.removeEventListener('keydown',key)}
}
function startShooter(){
 base('shooter','🛸 جنگنده کهکشانی');
 const stage=document.getElementById('stage');
 stage.innerHTML='<div class="shooter-wrap" id="shooterWrap"><canvas id="shootCanvas" width="340" height="460" aria-label="میدان نبرد فضایی؛ بدون کنترل یا جوی‌استیک روی میدان"></canvas></div><div class="shooter-controls"><button class="shooter-fire" id="shooterFire" aria-label="شلیک مداوم">🔥<span>شلیک مداوم</span></button><div class="shooter-tip">🚀 برای حرکت، انگشتت را روی میدان بکش؛ هیچ دکمه یا جوی‌استیکی داخل میدان نمایش داده نمی‌شود. دکمه شلیک پایین میدان است.</div></div><p>دشمن‌ها را نابود کن، از برخورد دوری کن و امتیازت را بالا ببر!</p>';
 const wrap=document.getElementById('shooterWrap'),c=document.getElementById('shootCanvas'),ctx=c.getContext('2d'),fireBtn=document.getElementById('shooterFire');
 let x=170,y=390,shots=[],enemies=[],alive=true,last=0,elapsed=0,spawn=0,raf=0,fireHeld=false,fireClock=0,scoreLocal=0,keys={},enemyLevel=1,lastAnnouncedLevel=1,movePointer=null,targetX=null,targetY=null;
 function coords(e){const r=c.getBoundingClientRect();return {x:(e.clientX-r.left)*c.width/r.width,y:(e.clientY-r.top)*c.height/r.height}}
 function moveDown(e){if(!alive)return;e.preventDefault();movePointer=e.pointerId;const p=coords(e);targetX=p.x;targetY=p.y;c.setPointerCapture?.(e.pointerId)}
 function moveDrag(e){if(movePointer!==e.pointerId)return;e.preventDefault();const p=coords(e);targetX=p.x;targetY=p.y}
 function moveUp(e){if(movePointer===e.pointerId)movePointer=null}
 c.addEventListener('pointerdown',moveDown);c.addEventListener('pointermove',moveDrag);c.addEventListener('pointerup',moveUp);c.addEventListener('pointercancel',moveUp);
 function fireDown(e){e.preventDefault();fireHeld=true;fireBtn.setPointerCapture?.(e.pointerId)}function fireUp(){fireHeld=false}
 fireBtn.addEventListener('pointerdown',fireDown);fireBtn.addEventListener('pointerup',fireUp);fireBtn.addEventListener('pointercancel',fireUp);fireBtn.addEventListener('pointerleave',fireUp);
 function keydown(e){if(['ArrowLeft','ArrowRight','ArrowUp','ArrowDown',' ','a','d','w','s'].includes(e.key))e.preventDefault();keys[e.key]=true;if(e.key===' ')fireHeld=true}
 function keyup(e){keys[e.key]=false;if(e.key===' ')fireHeld=false}
 window.addEventListener('keydown',keydown);window.addEventListener('keyup',keyup);
 function shoot(){shots.push({x,y:y-24})}
 function endGame(){alive=false;fireHeld=false;stage.insertAdjacentHTML('beforeend','<div class="game-over-card"><strong>💥 جنگنده آسیب دید!</strong><span>امتیاز نهایی: '+fa(scoreLocal)+'</span><button class="primary" onclick="restartGame()">🚀 تلاش دوباره</button></div>')}
 function frame(t){
  if(!alive)return;if(!last)last=t;const dt=Math.min((t-last)/1000,.04);last=t;elapsed+=dt;spawn+=dt;fireClock+=dt;
  enemyLevel=Math.min(10,1+Math.floor(elapsed/20));if(enemyLevel>lastAnnouncedLevel){lastAnnouncedLevel=enemyLevel;wrap.style.boxShadow='0 0 28px #ff547888';setTimeout(()=>{if(wrap.isConnected)wrap.style.boxShadow=''},550)}
  if(spawn>Math.max(.42,1.18-elapsed*.009)){spawn=0;const elite=enemyLevel>=3&&Math.random()<Math.min(.12+(enemyLevel-3)*.035,.35);const hp=enemyLevel+(elite?enemyLevel:0);enemies.push({x:22+Math.random()*296,y:-26,hp,maxHp:hp,level:enemyLevel,elite,phase:Math.random()*6,speed:(.8+Math.random()*.45)*(1+(enemyLevel-1)*.075)})}
  let ax=0,ay=0;if(keys.ArrowLeft||keys.a)ax=-1;if(keys.ArrowRight||keys.d)ax=1;if(keys.ArrowUp||keys.w)ay=-1;if(keys.ArrowDown||keys.s)ay=1;
  if(movePointer!==null&&targetX!==null){x+=(targetX-x)*Math.min(1,dt*13);y+=(targetY-y)*Math.min(1,dt*13)}
  else{x+=ax*205*dt;y+=ay*205*dt}
  x=Math.max(18,Math.min(322,x));y=Math.max(45,Math.min(420,y));
  if(fireHeld&&fireClock>.17){shoot();fireClock=0}
  shots.forEach(a=>a.y-=380*dt);enemies.forEach(a=>{a.y+=(72+Math.min(elapsed*1.8,115))*a.speed*dt;a.x+=Math.sin(elapsed*2.3+a.phase)*30*dt});shots=shots.filter(a=>a.y>-20);enemies=enemies.filter(a=>a.y<490);
  for(let i=enemies.length-1;i>=0;i--){const a=enemies[i],j=shots.findIndex(b=>Math.hypot(b.x-a.x,b.y-a.y)<19);if(j>=0){shots.splice(j,1);a.hp--;if(a.hp<=0){enemies.splice(i,1);scoreLocal+=10;setScore(scoreLocal)}}else if(Math.hypot(x-a.x,y-a.y)<25){endGame();return}}
  ctx.fillStyle='#030816';ctx.fillRect(0,0,340,460);
  for(let i=0;i<80;i++){const sx=(i*83)%340,sy=(i*59+elapsed*(22+(i%4)*10))%460;ctx.fillStyle=i%5===0?'#67eaff':'#7f91c5';ctx.globalAlpha=.3+(i%4)*.17;ctx.fillRect(sx,sy,i%5===0?2:1,i%5===0?3:1)}ctx.globalAlpha=1;
  const planetY=75+Math.sin(elapsed*.25)*5;ctx.fillStyle='#152b57';ctx.beginPath();ctx.arc(285,planetY,34,0,Math.PI*2);ctx.fill();ctx.strokeStyle='#52e7ff';ctx.globalAlpha=.4;ctx.beginPath();ctx.ellipse(285,planetY,48,12,-.3,0,Math.PI*2);ctx.stroke();ctx.globalAlpha=1;
  ctx.shadowColor='#51edff';ctx.shadowBlur=20;ctx.fillStyle='#ff9dff';ctx.beginPath();ctx.moveTo(x-6,y+13);ctx.lineTo(x,y+31+Math.random()*5);ctx.lineTo(x+6,y+13);ctx.fill();ctx.fillStyle='#52e7ff';ctx.beginPath();ctx.moveTo(x,y-24);ctx.lineTo(x-19,y+18);ctx.lineTo(x-5,y+12);ctx.lineTo(x,y+19);ctx.lineTo(x+5,y+12);ctx.lineTo(x+19,y+18);ctx.closePath();ctx.fill();ctx.shadowBlur=0;ctx.fillStyle='#f5fbff';ctx.fillRect(x-3,y-8,6,17);
  shots.forEach(a=>{ctx.fillStyle='#ffdb62';ctx.shadowColor='#ffdb62';ctx.shadowBlur=10;ctx.fillRect(a.x-2,a.y,4,14)});ctx.shadowBlur=0;
  for(const a of enemies){const size=12+Math.min(a.level,8)*.8;ctx.fillStyle=a.elite?'#b46cff':a.level>=6?'#ff354f':a.level>=3?'#ff9d42':'#ff4d78';ctx.shadowColor=ctx.fillStyle;ctx.shadowBlur=10+Math.min(a.level,8)*1.5;ctx.beginPath();ctx.moveTo(a.x,a.y+size);ctx.lineTo(a.x-size,a.y-size*.5);ctx.lineTo(a.x-size*.35,a.y-size*.35);ctx.lineTo(a.x,a.y-size);ctx.lineTo(a.x+size*.35,a.y-size*.35);ctx.lineTo(a.x+size,a.y-size*.5);ctx.closePath();ctx.fill();ctx.fillStyle='#fff0b7';ctx.fillRect(a.x-3,a.y-2,6,3);if(a.maxHp>1){ctx.shadowBlur=0;ctx.fillStyle='#401326';ctx.fillRect(a.x-size,a.y-size-7,size*2,3);ctx.fillStyle=a.elite?'#d9a8ff':'#ff7b94';ctx.fillRect(a.x-size,a.y-size-7,size*2*Math.max(0,a.hp/a.maxHp),3)}}ctx.shadowBlur=0;
  ctx.fillStyle='#eaf4ff';ctx.font='bold 13px Tahoma';ctx.fillText('امتیاز: '+scoreLocal,12,22);ctx.fillStyle=enemyLevel>=7?'#ff5478':enemyLevel>=4?'#ffb14e':'#67eaff';ctx.fillText('سطح دشمنان: '+enemyLevel,210,22);ctx.fillStyle='#ff7195';ctx.fillRect(12,31,Math.max(0,100-Math.min(100,elapsed*1.5)),4);raf=requestAnimationFrame(frame)
 }
 raf=requestAnimationFrame(frame);
 cleanup=()=>{alive=false;fireHeld=false;cancelAnimationFrame(raf);window.removeEventListener('keydown',keydown);window.removeEventListener('keyup',keyup);c.removeEventListener('pointerdown',moveDown);c.removeEventListener('pointermove',moveDrag);c.removeEventListener('pointerup',moveUp);c.removeEventListener('pointercancel',moveUp);fireBtn.removeEventListener('pointerdown',fireDown);fireBtn.removeEventListener('pointerup',fireUp);fireBtn.removeEventListener('pointercancel',fireUp);fireBtn.removeEventListener('pointerleave',fireUp)}
}

filterGames();
</script>
</body></html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
