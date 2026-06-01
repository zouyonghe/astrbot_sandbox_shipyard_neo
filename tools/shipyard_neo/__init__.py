from .browser import BrowserBatchExecTool, BrowserExecTool, RunBrowserSkillTool
from .neo_skills import (
    AnnotateExecutionTool,
    CreateSkillCandidateTool,
    CreateSkillPayloadTool,
    EvaluateSkillCandidateTool,
    GetExecutionHistoryTool,
    GetSkillPayloadTool,
    ListSkillCandidatesTool,
    ListSkillReleasesTool,
    PromoteSkillCandidateTool,
    RollbackSkillReleaseTool,
    SyncSkillReleaseTool,
)

SHIPYARD_NEO_TOOL_MODULE_PREFIX = __name__
BROWSER_TOOL_CLASSES = (
    BrowserExecTool,
    BrowserBatchExecTool,
    RunBrowserSkillTool,
)
NEO_SKILL_TOOL_CLASSES = (
    GetExecutionHistoryTool,
    AnnotateExecutionTool,
    CreateSkillPayloadTool,
    GetSkillPayloadTool,
    CreateSkillCandidateTool,
    ListSkillCandidatesTool,
    EvaluateSkillCandidateTool,
    PromoteSkillCandidateTool,
    ListSkillReleasesTool,
    RollbackSkillReleaseTool,
    SyncSkillReleaseTool,
)
SHIPYARD_NEO_TOOL_CLASSES = (*BROWSER_TOOL_CLASSES, *NEO_SKILL_TOOL_CLASSES)
SHIPYARD_NEO_TOOL_NAMES = frozenset(
    tool_cls.name for tool_cls in SHIPYARD_NEO_TOOL_CLASSES
)
BROWSER_TOOL_NAMES = frozenset(tool_cls.name for tool_cls in BROWSER_TOOL_CLASSES)


def should_enable_browser_tools(profile: str | None) -> bool:
    normalized = str(profile or "").strip()
    return normalized != "python-default"


def tool_classes_for_profile(profile: str | None):
    if should_enable_browser_tools(profile):
        return SHIPYARD_NEO_TOOL_CLASSES
    return NEO_SKILL_TOOL_CLASSES


def tool_names_for_profile(profile: str | None) -> frozenset[str]:
    return frozenset(tool_cls.name for tool_cls in tool_classes_for_profile(profile))


def build_shipyard_neo_tools(profile: str | None = None):
    return [tool_cls() for tool_cls in tool_classes_for_profile(profile)]


__all__ = [
    "AnnotateExecutionTool",
    "BROWSER_TOOL_CLASSES",
    "BROWSER_TOOL_NAMES",
    "BrowserBatchExecTool",
    "BrowserExecTool",
    "CreateSkillCandidateTool",
    "CreateSkillPayloadTool",
    "EvaluateSkillCandidateTool",
    "GetExecutionHistoryTool",
    "GetSkillPayloadTool",
    "ListSkillCandidatesTool",
    "ListSkillReleasesTool",
    "PromoteSkillCandidateTool",
    "RollbackSkillReleaseTool",
    "RunBrowserSkillTool",
    "NEO_SKILL_TOOL_CLASSES",
    "SyncSkillReleaseTool",
    "SHIPYARD_NEO_TOOL_CLASSES",
    "SHIPYARD_NEO_TOOL_MODULE_PREFIX",
    "SHIPYARD_NEO_TOOL_NAMES",
    "build_shipyard_neo_tools",
    "should_enable_browser_tools",
    "tool_classes_for_profile",
    "tool_names_for_profile",
]
