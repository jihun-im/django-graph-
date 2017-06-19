import GoogleLoginAndGetRestApiJson
import plotly.graph_objs as go
from plotly.offline import plot

service, flags = GoogleLoginAndGetRestApiJson.loginToGoogleForUrlShortenerApi()
dateList, clickCountList = GoogleLoginAndGetRestApiJson.getList(service, flags)

trace1 = go.Scatter(
    x=dateList,
    y=clickCountList,
    mode='lines',
    name='clicks',
)

data = [trace1, ]

# Edit the layout
layout = dict(title='IT 뉴스방 조회 수 체크 (https://open.kakao.com/o/ghVKecp)',
              xaxis=dict(title='Date'),
              yaxis=dict(title='조회 수'),
              bargap=0.5
              )

fig = dict(data=data, layout=layout)

plot(
    figure_or_data=fig,
    filename='urllistgraph.html',
)

# help(plotly.offline.plot)
