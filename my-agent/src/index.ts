import { Agent, run, user } from '@openai/agents';
import type { AgentInputItem } from '@openai/agents';
import readline from 'node:readline/promises';

const agent = new Agent({
  name: 'Chatbot',
  instructions: 'You are a helpful assistant. Be concise and friendly.',
  model: 'gpt-4o-mini',
});

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let history: AgentInputItem[] = [];

console.log('Chatbot ready. Type "exit" to quit.\n');

while (true) {
  const input = await rl.question('You: ');
  if (input.toLowerCase() === 'exit') break;

  history.push(user(input));
  const result = await run(agent, history);
  history = result.history;

  console.log(`\nBot: ${result.finalOutput}\n`);
}

rl.close();
