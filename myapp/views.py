import re
from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from dotenv import dotenv_values
from openai import OpenAI
env_variables = dotenv_values()

client = OpenAI(
    api_key=env_variables['OPENAI_API_KEY'],
)



def generate_blog_post(topic: str):
    """Generate a blog post from a given topic using OpenAI"""
    prompt = f"""
    You will be writing a well-researched blog on this topic "{topic}" based on the below instructions-

    Think of the angles which are important but often overlooked, pick 5 such themes, analyze which of the theme will be most relevant,

    Based on this theme create a list of keywords that are most expected to be used by a user when searching for similar topics,

    Once this is done create an outline for the blog, follow the below instructions when writing a segment from the outline.

    1. Start with a hook. Brainstorm a first sentence or subheading that is eye-catching, short, and memorable. Start with a description of the problem or a rhetorical question for your readers. Your title should also draw readers in, but don't worry about the post title early in the outlining process—use a working title to save time while you outline and work on the first draft.
    2. Set up the purpose. All blog posts have a purpose—whether that's persuasive (proving a claim) or informational (offering knowledge on a topic). State your purpose early in your intro so readers know what to expect from your blog content. The introduction sets the tone for the blog post and offers vital background information or historical context for your target audience.
    3. Outline key info with bulleted points. A blog outline helps you see how to order your main points and where you can break information into sections with subheadings. Outline your main points in a bulleted list to decide the best order for the information and to avoid writing fluff that doesn't relate to your argument.
    4. Wrap up with a conclusion. When you conclude your blog post, offer readers a key takeaway (called a CTA). End with a memorable final line—something hard-hitting or clever that ties your work up neatly or a question for further discussion in the comments.

    Proofread to make sure it doesn't sound robotic and also it doesn't sound like a pseudo human.

    We can have 4 subheadings, each to have 200-300 words.

    """
    
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    # Extract the generated blog content
    blog_content = response.choices[0].message.content
    blog_lines = blog_content.split("\n")
    
    # Extract and clean the title
    raw_title = blog_lines[0].strip().lstrip('#').strip()
    title = re.sub(r'<[^>]+>', '', raw_title).replace('**', '').strip()
    content = "\n".join(blog_lines[1:]).strip()


    return title, content


class BlogGeneratorView(APIView):
    """API endpoint to generate a blog from a given topic"""

    def post(self, request, format=None):
        topic = request.data.get("topic", "").strip()
        if not topic:
            return Response({"error": "Topic is required."}, status=400)

        try:
            title, content = generate_blog_post(topic)
            return Response({
                "title": title,
                "topic": topic,
                "content": content
            }, status=200)
        except Exception as e:
            return Response({"error": str(e)}, status=500)
