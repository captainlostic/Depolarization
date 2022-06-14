repeat task.wait() until game:IsLoaded()

local WebSocket = syn.websocket.connect("ws://localhost:9999")

game:GetService('CoreGui').DescendantAdded:Connect(function(Obj)
    if (Obj.Name == 'ErrorMessage' and Obj:IsA('TextLabel')) then 
        repeat game:GetService('RunService').Heartbeat:Wait() until (string.match(Obj.Text, 'unexpected') or string.match(Obj.Text, 'internet'));
        WebSocket:Send('Switch');
        while task.wait(4) do
            game:GetService('TeleportService'):Teleport(3016661674);
        end;
    end;
end)

repeat task.wait() until (game:IsLoaded());
for i,v in pairs(getconnections(game:GetService('Players').LocalPlayer.Idled)) do
    v:Disable();
end;