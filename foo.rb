[
  "analysis",
  "decomposing the system",
  "addressing design goals",
  "reusing pattern solutions",
  "specifying intrefaces",
  "mapping models to code",
  "testing",
  "rationale managemtn",
  "configruation management",
  "project management",
  "software life cycle",
  "putting it all together",
].each.with_index do |word, i|
  puts "touch #{i+5}-#{word.downcase.gsub(/\s/, "-")}"
end
