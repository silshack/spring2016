require 'html/proofer' 

task :test do
  sh 'echo "\n\nbaseurl:\nurl:" >> _config.yml'
  begin
    sh "bundle exec jekyll build"
    HTML::Proofer.new("./_site", {:href_swap => {/\/spring2016\// => "/"}, :disable_external => true, :checks_to_ignore => ['ScriptCheck'], :empty_alt_ignore => true, :verbose => true}).run
  rescue Exception => e  
    puts e.message  
    puts e.backtrace.inspect  
  end 
  sh 'head -n -4 _config.yml > tmp && mv tmp _config.yml'
end
