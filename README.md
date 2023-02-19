# NoteUp
Hack NYU 2023 submission from Team NoteUp.

## Running the code:
- Login to https://platform.openai.com/playground
- Generate your own secret API key through the profile tab
- Create a .env file and add your secret key as the 'API_KEY'
- Clone this repository into the same directory and run it with Python

## Inspiration
As graduate students, we understand the stress of assignment deadlines and finals week. When you're looking for jobs along with trying to manage your workload, it is easy to get overwhelmed. NoteUp helps you organize your lectures, ppts, and other forms of notes into a concise summary that helps you better understand what has been taught and be up to date. It takes the stress off your head and does half the job for you. All you have to do is sit down and study!

## What it does
NoteUp allows users to easily organize, edit, and access their notes from any device, making it an ideal tool for individuals, students, and teams. With its focus on simplicity and productivity, NoteUp helps users take better notes and get more done.

## How we built it
We integrated ChatGPT with Python using OpenAPI to summarize the payload we pass to it. In Python, we use Tkinter package to create a GUI that allows users to upload files they would like to summarize and then lets you download a file containing the condensed notes into a pre-defined output directory.

## Challenges we ran into
The main challenge was training data to create our own summarizing model since we didn't have the resources available to train huge datasets (required for acceptable accuracy). Thus, we decided to use ChatGPT to perform the summarizing functionality. This posed the challenge of having a strict limit on the number of tokens that can be parsed in one pass.

## Accomplishments that we're proud of
We are proud to be able to digitally prototype our web application using Figma. Moreover, we have also created a Proof of Concept to demo its functioning.

## What we learned
We learned that students across different levels of education, schools, and countries struggle with note-taking, especially when they are expected to refer to different sources for each subject. We hope NoteUp will alleviate some of this stress if not all.

In technical terms, we learned how to build GUI within Python itself and also leverage opensource APIs.

## What's next for NoteUp.
NoteUp may add new features to enhance the user experience and differentiate itself from other note-taking apps. For example, it could add features like voice-to-text transcription (for recorded classes), AI-powered note recommendations, or integration with popular task management tools.

It could also integrate with other productivity tools, such as calendar apps, project management software, or email clients. This would make it easier for users to integrate note-taking into their existing workflows.

