from google.ai.generativelanguage_v1beta.types import content

reformat_table_config = {
    "model_name": "gemini-1.5-flash-002",
    "generation_config": {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 8192,
        "response_schema": content.Schema(
            type = content.Type.OBJECT,
            required = ["reformat"],
            properties = {
                "reformat": content.Schema(
                    type = content.Type.STRING,
                )
            },
        ),
        "response_mime_type": "application/json",
    }
}

double_check_config = {
    "model_name": "gemini-1.5-pro-002",
    "generation_config": {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 8192,
        "response_schema": content.Schema(
            type = content.Type.OBJECT,
            required = ["return"],
            properties = {
                "return": content.Schema(
                    type = content.Type.BOOLEAN,
                ),
            },
        ),
        "response_mime_type": "application/json",
    }
}

crop_config = {
    "model_name": "gemini-1.5-pro-002",
    "generation_config": {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 8192,
        "response_schema": content.Schema(
            type = content.Type.OBJECT,
            required = ["x_min", "y_min", "x_max", "y_max"],
            properties = {
                "x_min": content.Schema(
                    type = content.Type.NUMBER,
                ),
                "y_min": content.Schema(
                    type = content.Type.NUMBER,
                ),
                "x_max": content.Schema(
                    type = content.Type.NUMBER,
                ),
                "y_max": content.Schema(
                    type = content.Type.NUMBER,
                ),
            },
        ),
        "response_mime_type": "application/json",
    }
}

extract_affiliation_config = {
    "model_name": "gemini-1.5-flash-8b",
    "generation_config": {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 8192,
        "response_schema": content.Schema(
            type = content.Type.OBJECT,
            required = ["affiliation"],
            properties = {
                "affiliation": content.Schema(
                    type = content.Type.STRING,
                ),
            },
        ),
        "response_mime_type": "application/json",
    }
}

extract_category_config = {
    "model_name": "gemini-1.5-flash-8b",
    "generation_config": {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 8192,
        "response_schema": content.Schema(
            type = content.Type.OBJECT,
            required = ["main_category", "sub_category"],
            properties = {
                "main_category": content.Schema(
                    type = content.Type.STRING,
                ),
                "sub_category": content.Schema(
                    type = content.Type.STRING,
                ),
            },
        ),
        "response_mime_type": "application/json",
    }
}

extract_essentials_config = {
    "model_name": "gemini-1.5-flash-002",
    "generation_config": {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 8192,
        "response_schema": content.Schema(
            type = content.Type.OBJECT,
            required = ["summary", "tldr", "takeaways", "importance"],
            properties = {
                "summary": content.Schema(
                    type = content.Type.STRING,
                ),
                "tldr": content.Schema(
                    type = content.Type.STRING,
                ),
                "takeaways": content.Schema(
                    type = content.Type.ARRAY,
                    items = content.Schema(
                        type = content.Type.STRING,
                    ),
                ),
                "importance": content.Schema(
                    type = content.Type.STRING,
                ),
            },
        ),
        "response_mime_type": "application/json",
    }
}

extract_references_config = {
    "model_name": "gemini-1.5-flash-002",
    "generation_config": {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 8192,
        "response_schema": content.Schema(
            type = content.Type.OBJECT,
            required = ["references"],
            properties = {
                "references": content.Schema(
                    type = content.Type.ARRAY,
                    items = content.Schema(
                        type = content.Type.OBJECT,
                        required = ["paper_title", "fullname_first_author", "publication_date", "reason"],
                        properties = {
                            "paper_title": content.Schema(
                                type = content.Type.STRING,
                            ),
                            "fullname_first_author": content.Schema(
                                type = content.Type.STRING,
                            ),
                            "publication_date": content.Schema(
                                type = content.Type.STRING,
                            ),
                            "reason": content.Schema(
                                type = content.Type.STRING,
                            ),
                        },
                    ),
                ),
            },
        ),
        "response_mime_type": "application/json",
    }
}

extract_sections_config = {
    "model_name": "gemini-1.5-flash-002",
    "generation_config": {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 8192,
        "response_schema": content.Schema(
            type = content.Type.OBJECT,
            required = ["sections"],
            properties = {
                "sections": content.Schema(
                    type = content.Type.ARRAY,
                    items = content.Schema(
                        type = content.Type.OBJECT,
                        required = ["heading_title"],
                        properties = {
                            "heading_title": content.Schema(
                                type = content.Type.STRING,
                            ),
                        },
                    ),
                ),
            },
        ),
        "response_mime_type": "application/json",
    }
}

extract_section_details_config = {
    "model_name": "gemini-1.5-flash-002",
    "generation_config": {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 8192,
        "response_schema": content.Schema(
            type = content.Type.OBJECT,
            required = ["summary"],
            properties = {
                "summary": content.Schema(
                    type = content.Type.STRING,
                ),
            },
        ),
        "response_mime_type": "application/json",
    }
}

write_script_config = {
    "model_name": "gemini-1.5-flash-002",
    "generation_config": {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 8192,
        "response_schema": content.Schema(
            type=content.Type.OBJECT,
            required=["conversations"],
            properties={
                "conversations": content.Schema(
                    type=content.Type.ARRAY,
                    items=content.Schema(
                        type=content.Type.OBJECT,
                        required=["Alex", "Jamie"],
                        properties={
                            "Alex": content.Schema(
                                type=content.Type.STRING,
                            ),
                            "Jamie": content.Schema(
                                type=content.Type.STRING,
                            ),
                        },
                    ),
                ),
            },
        ),
        "response_mime_type": "application/json",
    }
}
