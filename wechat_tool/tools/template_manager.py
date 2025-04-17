from typing import Dict, Any
from jinja2 import Environment, FileSystemLoader, select_autoescape
from htmlmin import minify

class TemplateManager:
    def __init__(self, templates_dir: str = "templates"):
        self.templates_dir = templates_dir
        self.env = Environment(
            loader=FileSystemLoader(templates_dir),
            autoescape=select_autoescape(['html']),
            # 空白控制相关
            trim_blocks=True,      # 移除块级标签后的第一个换行符
            lstrip_blocks=True,    # 移除块级标签前的空白字符
            keep_trailing_newline=False,  # 不保留末尾换行符
        )
    
    def render_template(self, template_id: str, data: Dict[str, Any]) -> str:
        """渲染模板"""
        template = self.env.get_template(f"{template_id}.html")
        rendered = template.render(**data)
        # 压缩 HTML
        return minify(rendered,
            remove_empty_space=True,      # 移除多余空格
            remove_all_empty_space=False, # 不移除所有空格
            remove_comments=True,         # 移除注释
            remove_optional_attribute_quotes=False  # 保留属性引号
        ) 