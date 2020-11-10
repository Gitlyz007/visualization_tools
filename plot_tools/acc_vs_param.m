% WS 
x = [log10(26.8),log10(28.6),log10(29.5)];%param
y = [0.950283,0.953674,0.960893];%acc
plot(x,y,'MarkerFaceColor',[255 128 64]/255,...
    'MarkerEdgeColor',[0 0 0],...
    'MarkerSize',10,...
    'Marker','o',...
    'LineWidth',2,...
    'Color',[188 98 48]/255); hold on

c = ['1','2','3'];
% c = ['-baseline','+ResNet','+ResNet+BiT-M'];
offset1 = [0 0 0];
offset2 = [0 0 0];
for i = 1:numel(c)
    text(x(i)+offset1(i),y(i)+offset2(i),['WS-DAN' c(i)], 'FontName','Times New Roman','FontSize',12);
end


% MobileNetV1,V3
x = [log10(4.2),log10(2.9)];%param
y = [0.874662,0.883745];%acc
plot(x,y,'MarkerFaceColor',[0 128 224]/255,...
    'MarkerEdgeColor',[0 0 0],...
    'MarkerSize',10,...
    'Marker','o',...
    'LineWidth',2,...
    'Color',[166 200 254]/255); hold on

c = [1 3];
offset1 = [0 0];
offset2 = [0 0];
for i = 1:numel(c)
    text(x(i)+offset1(i),y(i)+offset2(i),['MobileNet-V' num2str(c(i))], 'FontName','Times New Roman','FontSize',12);
end

% ResNet 50 101
x = [log10(25),log10(44)];%param
y = [0.876097,0.889154];%acc
plot(x,y,'MarkerFaceColor',[0 162 23]/255,...
    'MarkerEdgeColor',[0 0 0],...
    'MarkerSize',10,...
    'Marker','o',...
    'LineWidth',2,...
    'Color',[96 224 94]/255); hold on

c = [50 101];
offset1 = [0 0];
offset2 = [0 0];
for i = 1:numel(c)
    text(x(i)+offset1(i),y(i)+offset2(i),['ResNet-' num2str(c(i))], 'FontName','Times New Roman','FontSize',12);
end

%VGG 16 19
x = [log10(138),log10(143)];%param
y = [0.904338,0.896071];%acc
plot(x,y,'MarkerFaceColor',[189,88,188]/255,...
    'MarkerEdgeColor',[0 0 0],...
    'MarkerSize',10,...
    'Marker','o',...
    'LineWidth',2,...
    'Color',[191,128,209]/255)  
hold on;
c = [16 19];
offset1 = [0.1 0.1];
offset2 = [0.0 0.0];
for i = 1:numel(c)
    text(x(i)+offset1(i),y(i)+offset2(i),['VGG-' num2str(c(i))],'FontName','Times New Roman','FontSize',12);
end

%InceptionV1 V3 V4
x = [log10(25.1),log10(23.2),log10(21.3)];%param
y = [0.912076,0.928497, 0.917873];%acc
plot(x,y,'MarkerFaceColor',[206,128,138]/255,...
    'MarkerEdgeColor',[0 0 0],...
    'MarkerSize',10,...
    'Marker','o',...
    'LineWidth',2,...
    'Color',[198,128,134]/255)  
hold on;
c = [1 3 4];
offset1 = [0.1 0.1 0.1];
offset2 = [0.0 0.0 0.0];
for i = 1:numel(c)
    text(x(i)+offset1(i),y(i)+offset2(i),['Inception-V' num2str(c(i))],'FontName','Times New Roman','FontSize',12);
end

%EfficientNet b0 b4 b5 b7
x = [log10(5.3),log10(19),log10(30),log10(84.4)];%param
y = [0.919975,0.940552, 0.932862, 0.932862];%acc
plot(x,y,'MarkerFaceColor',[255,208,64]/255,...
    'MarkerEdgeColor',[0 0 0],...
    'MarkerSize',10,...
    'Marker','o',...
    'LineWidth',2,...
    'Color',[245,214,178]/255)  
hold on;
c = [0 4 5 7];
offset1 = [0.1 0.1 0.1 0.1];
offset2 = [0.0 0.0 0.0 0.0];
for i = 1:numel(c)
    text(x(i)+offset1(i),y(i)+offset2(i),['EfficientNet-b' num2str(c(i))],'FontName','Times New Roman','FontSize',12);
end



grid on
set(gca,'linewidth',1,'GridLineStyle',':','YTick',[0.86 0.87 0.88 0.89 0.90 0.91 0.92 0.93 0.94 0.95 0.96 0.97])
ylim([0.86,0.97]);
set(gca,'linewidth',1,'GridLineStyle',':','XTick',[0.25 0.5 0.75 1 1.25 1.5 1.75 2 2.25 2.5])
xlim([0.25,2.5]);
xlabel('Parameters(10^x)', 'FontName','Times New Roman');
ylabel('Accuracy', 'FontName','Times New Roman');
title('Accuracy v.s. Model Size', 'FontName','Times New Roman','FontSize',14)
legend({ 'WS-DAN Series', 'MobileNet Series', 'ResNet Series', 'VGG Series','Inception Series','EfficientNet Series'},...
    'Location','northwest','Interpreter','latex','FontSize',12)
set(gcf, 'position', [500 300 700 550]);
saveas(gcf,'../img/acc_vs_param','pdf');
saveas(gcf,'../img/acc_vs_param','png');
