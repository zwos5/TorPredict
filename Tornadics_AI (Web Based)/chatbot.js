function talk() {
prompt = document.form1.user.value;

let prompts = ["Hi.", "How's it going?",
"Tell me about", "Rain.", "Thunderstorms.", 
"Tornadoes.", "Snow.", "Windy.", "Hail.", 
"Hurricanes.", "What is your name?", "Do you do anything besides weather?",
"Has anyone said thank you?", "Thank you.", 
"What is the record amount of rainfall?", 
"What is the record amount of snowfall?"]

let responses = ["Hello!", "I'm doing good, how about you?",
"What would you like to know about?", 
"Rain is water that has accumulated up in the atmosphere of the earth that falls when it gets heavy.",
"A thunderstorm occurs when the air is humid and hot or cold air moves in to an area where it currently hot/cold depending on the season.",
"A tornado is a violently rotating column of air that happens when two different air temperatures begin blowing in opposite directions",
"Snow is like rain in a frozen form",
"A windy day occurs when air begins moving at a quick rate of speed",
"Hail is rain that has frozen up in the atmosphere during a thunderstorm",
"A hurricane is similar in ways to a tornado. However, hurricanes are characterized by a low-pressure center, a closed low-level atmospheric circulation, strong winds, and a spiral arrangement of thunderstorms that produce heavy rain and squalls.",
"My name is Tornadics.ai I can tell you about the weather", "Not at this time but maybe in the future",
"As a robot I don't look too much into manners as long as I know I'm being helpful that's what counts.",
"You're welcome user, glad I could help.", 
"71.8 inches in on the French island territory of Reunion on January 7-8 1966.",
"390 inches (32.5 feet) in Tamarack California in January 1911"]

const label = "=====================================================================================================[EF LEVELS]================================================================================";
const efu = "EFU: Wind Speed: N/A Frequency: 3.11%: Usually no surveyable damage and intensity likely cannot be determined due to either a lack of information or winds weren't fast enough to cause damage.";
const ef0 = "EF0: Wind Speed: 65-85mph Frequency: 52.82%: Some minor damage mostly among trees, old unrepaired buildings, windows, shingles, or loose small items.";
const ef1 = "EF1: Wind Speed: 86-110mph Frequency: 32.98%: Moderate damage roofs will be stripped of shingles, mobile homes flipped, and doors and garage doors blown in.";
const ef2 = "EF2: Wind Speed: 111-135mph Frequency: 8.41%: Considerable damage whole roofs ripped off of frame houses, interiors of frame homes destroyed, weak structures completely destroyed.";
const ef3 = "EF3: Wind Speed: 136-165mph Frequency: 2.18%: Severe damage roofs and other walls blown away, multi-story homes have upper floors destroyed.";
const ef4 = "EF4: Wind Speed: 166-200mph Frequency: 0.46%: Devastating damage trees debarked partially, cars thrown, frame homes destroyed, moving trains blown off of tracks.";
const ef5 = "EF5: Wind Speed: >200mph Frequency: 0.05%: Incredible damage cars are destroyed and thrown hundreds of yards away from their starting location, any type of home is likely destroyed, corn fields flattened, skyscrapers suffer damage.";
const chart = label + "\n" + efu + "\n" + ef0 + "\n" + ef1 + "\n" + ef2 + "\n" + ef3 + "\n" + ef4 + "\n" + ef5;

for(var i = 0; i <= prompts.length; i++) {
	if(prompts.includes(prompt)){
			bot_chat = prompts.indexOf(prompt);
			document.form1.response.value = responses[bot_chat];
	}
	else {
			document.form1.response.value = "Sorry I didn't get that perhaps it will be here in a future update.";
	}
	if(prompt == "Tornadoes.") {
			document.form1.tchart.value = chart;
			}
	else {
		document.form1.tchart.value = "";
	}
	}
}